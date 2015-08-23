from django.shortcuts import render
from brokers.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.sessions.models import Session
from brokers import utils

# Create your views here.
def registration(request):
    if request.method=='POST':
                  fname=request.POST['fname']
                  lname=request.POST['lname']
                  address=request.POST['address']
                  city=request.POST['city'],
                  state=request.POST['state']
                  country=request.POST['country']
                  pincode=request.POST['pincode']
                  contact_number=long(request.POST['contact_number'])
                  email=request.POST['email']
                  companyname=request.POST['company']
                  password=request.POST['password']
                  crpassword=request.POST['crpassword']
                  pincode,pincode_error=utils.verify_pincode(pincode)
                  contact_number,cont_error=utils.verify_mobile(contact_number)
                  email,email_error=utils.verify_email(email)
                  pwd,pwd_error=utils.verify_passwords(password,crpassword)
                   
                  if pincode!='-1'and contact_number!='-1'and email!='-1'and pwd!='-1':
                     obj=Broker_info(fname=fname,lname=lname,address=address,city=city,
                     state=state,country=country,pincode=pincode,contact_number=long(contact_number),email=email,password=password,companyname=companyname)
                     obj.save()
                     temp=Broker_info.objects.get(email=email)
                     request.session["uid"] =temp.id
                     return HttpResponseRedirect('/profile/')
                     
                  else:
                     return render(request,"registrationform.html",{"fname":fname,"lname":lname,"address":address,"city":city,
                     "state":state,"country":country,"pincode":pincode,"contact_number":long(contact_number),"email":email,"password":password,"pincode_error":pincode_error,"cont_error":cont_error,"email_error":email_error,"pwd_error":pwd_error})    
                
    else:   
            return render(request,"registrationform.html")

def profile(request):
            return HttpResponse("hello")