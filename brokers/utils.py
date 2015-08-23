import os
import cgi
import re
import random
import string
import datetime
import math

def verify_name(name):
	'''	Expected string inputs.
	   	Returns 
			- (name,'Success') -> if name is perfect. Will uppercase first letter.
			- ('-1',<error message>) -> if other characters found
		Will do HTML escaping on it.'''
	escaped_name = str(cgi.escape(name,quote="True"))
	if not escaped_name.isalpha():
		return ('-1','Name Contains invalid characters')
	else:
		return (name,'')

def verify_email(email):
	'''Expects valid email IDs
		Returns 
			- (email,'')
			- ('-1',<error>)'''
	match = re.search(r'[\w.-]+@[\w.-]+', email)
	if match:
		print match.group()
		return (str(match.group()),'')
	else:
		return ('-1','Invalid Email ID')

def verify_passwords(pwd,cpwd):
	if pwd == cpwd:
		if len(pwd) >= 6:
			return (pwd,'')
		else:
			return ('-1','Password too short!')
	else:
		return ('-1','Passwords do not match')

def verify_mobile(mobile):
	#expects string
	print "utils: verify_mobile: ", mobile
	try:
		mobile = long(mobile)
	except:
		print "utils: verify_mobile: mobile number is not integer ", mobile

	if mobile.__class__ == long(3).__class__:
		#successfully converted to long
		return (mobile,'')

	else:
		return ('-1',"Mobile number is a number")

def verify_pincode(pincode):
   
    length=len(pincode)
    if length==6:
         return (pincode,'')
    else:
         return ('-1','Wrong pincode')  
            		
def verify_text(text):
	return (text,'Success')

def encrypt(strng):
	return strng

def generate_string(size = 10, chars =  string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

 
 
