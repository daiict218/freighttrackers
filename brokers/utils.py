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
def verify_age(age):
   
    length=len(age)
    if length==2:
         return (age,'')
    else:
         return ('-1','Wrong age')          
            		
def verify_text(text):
	return (text,'Success')

def encrypt(strng):
	return strng

def generate_string(size = 10, chars =  string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def verify_driver(request):
         fname=request.POST['fname']
         lname=request.POST['lname']
         address=request.POST['address']
         city=request.POST['city']
         state=request.POST['state']
         country=request.POST['country']
         pincode=request.POST['pincode']
         contact_number=request.POST['contact_number']
         license_number=request.POST['licensenumber']
         age=request.POST['age']
         age,age_error=verify_age(age)
         pincode,pincode_error=verify_pincode(pincode)
         contact_number,cont_error=verify_mobile(contact_number)
         error=[]
         if fname=='':
             error.append("first name is required")
         if lname=='':
             error.append("last name is required")
         if address=='':
            error.append("address  is required")
         if city=='':
            error.append("city is required")
         if  state=='':
            error.append("state is required")
         if license_number=='':
            error.append("license is required")   
         if  country=='':
            error.append("country is required")                        
         if pincode=='-1':
            pincode=''
            error.append(pincode_error)
         if contact_number=='-1':
            contact_number=''
            error.append(cont_error)
         if age=='-1':
            age=''
            error.append(age_error)   
         return {"fname":fname,"lname":lname,"address":address,"city":city,"state":state,
         "pincode":pincode,"contact_number":contact_number,"error":error,"country":country,"age":age
         ,"license_number":license_number}    	

 
 
