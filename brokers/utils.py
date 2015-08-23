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
		return (name,'Success')

def verify_email(email):
	'''Expects valid email IDs
		Returns 
			- (email,'Success')
			- ('-1',<error>)'''
	match = re.search(r'[\w.-]+@[\w.-]+', email)
	if match:
		print match.group()
		return (str(match.group()),'Success')
	else:
		return ('-1','Invalid Email ID')

def verify_passwords(pwd,cpwd):
	if pwd == cpwd:
		if len(pwd) >= 6:
			return (pwd,'Success')
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
		return (mobile,'Success')

	else:
		return ('-1',"Mobile number is a number")

def verify_pincode(pincode):
   
    length=len(pincode)
    if length==6:
         return (pincode,'success')
    else:
         return ('-1','Wrong pincode')  
            		
def verify_text(text):
	return (text,'Success')

def encrypt(strng):
	return strng

def generate_string(size = 10, chars =  string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

 
 

def email_verification(shop,code):
	print "utils: emailverification: ",shop.shop_name,code
	
	mail.send_mail(sender= "store-locatr@appspot.gserviceaccount.com",
	              to= shop.email,
	              subject= "Account Verification",
	              body= """

	Dear %(name)s:

	Your store-locatr.appspot.com account is pending approval. For security purposes, your shop would not be shown to any user till you verify it.
	Should you choose to not do that at this point of time, you are advised to archive this email someplace retrievable and access the link given below later. 
	Till then you can set up your shop profile without any hinderances.

	Please visit this link to verify your shop now - http://store-locatr.appspot.com/shop/verify?code=%(code)s

	After doing that, you can sign in and make your profile visible to the entire internet audience.
	
	Please let us know if you have any questions.
	
	Following are the details of your shop.
	Shop Name -  %(shopname)s
	Shopkeeper Name - %(shopkeeper)s
	Shop Address - %(shopaddress)s

	If you did not reigster the above yourself, please ignore this mail and get on with your life.
	Alternatively you can always register to store-locatr.appspot.com/shop to make your retail store visible to a larger audience.
	And if you don't have a retail store, might as well take a step ahead and open one. Everyone needs their daily sugar afterall. 
		Once you complete that, do register your store with us.

	Regards
	Store Locator
	""" % {'name' : shop.fname, 'shopname' : shop.shop_name, 'shopkeeper' : shop.fname, 'shopaddress' : shop.shop_address, 'code': code} ) 

	print "Mail sent"