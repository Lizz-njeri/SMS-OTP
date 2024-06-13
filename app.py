import math
import random
import africastalking

from flask import Flask, render_template, request, redirect, url_for, session

# Initialize Africa's Talking
username = ""
api_key = ""
africastalking.initialize(username, api_key)
sms = africastalking.SMS

# Initialize Flask app
app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# Function to generate OTP
def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

# Route for signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        phone_number = request.form['phone_number']  # Assuming phone number is entered in the form
        session['email'] = email
        session['phone_number'] = phone_number

        # Generate OTP
        otp = generate_otp()
        session['otp'] = otp

        # Send OTP via SMS
        message = f"Your OTP for signup is {otp}"
        response = sms.send(message, [phone_number])
        print(response)  # Print the response for debugging purposes

        return redirect(url_for('verify'))

    return render_template('signup.html')

# Route for OTP verification
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        otp_entered = request.form['otp']
        otp_generated = session.get('otp')

        if otp_entered == otp_generated:
            # OTP is verified successfully
            return "OTP Verified. You can now login!"

        else:
            # Invalid OTP
            return "Invalid OTP. Please try again."

    return render_template('verify.html')

if __name__ == '__main__':
    app.run(debug=True)
