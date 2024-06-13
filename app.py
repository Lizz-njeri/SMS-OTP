# import library
import math, random
import africastalking

username = "ENTER_USERNAME"
api_key = "ENTER_API_KEY"
africastalking.initialize(username, api_key)
sms = africastalking.SMS
phone_number="YOUR_PHONE_NUMBER"

# function to generate OTP
def generateOTP() :

	# Declare a digits variable 
	# which stores all digits 
	digits = "0123456789"
	OTP = ""

# length of password can be changed
# by changing value in range
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]

	return OTP

# Driver code
if __name__ == "__main__" :
	otp=generateOTP()
	print(otp)
	response = sms.send(f"Your OTP is {otp}", [phone_number])
	print(response)
	
	
