from django.shortcuts import render
from brokers.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.sessions.models import Session
from brokers import utils
from django.core.mail import send_mail
import random

# Create your views here.
def registration(request):
    if request.method=='POST':
                  fname=request.POST['fname']
                  lname=request.POST['lname']
                  address=request.POST['address']
                  city=request.POST['city']
                  state=request.POST['state']
                  country=request.POST['country']
                  pincode=request.POST['pincode']
                  contact_number=long(request.POST['contact_number'])
                  email=request.POST['email']
                  companyname=request.POST['company']
                  password=request.POST['password']
                  crpassword=request.POST['crpassword']
                  print password
                  print crpassword
                  pincode,pincode_error=utils.verify_pincode(pincode)
                  contact_number,cont_error=utils.verify_mobile(contact_number)
                  email,email_error=utils.verify_email(email)
                  pwd,pwd_error=utils.verify_passwords(password,crpassword)
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
                  if companyname=='':
                       error.append("company name is required")                         
                  if pincode=='-1':
                       pincode=''
                       error.append(pincode_error)
                  if contact_number=='-1':
                       contact_number=''
                       error.append(cont_error)
                  if email=='-1':
                       email=''
                       error.append(email_error)          
                  if pwd=='-1':
                       pwd=''
                       error.append(pwd_error) 
                  if not error:
                    var=Broker_info.objects.filter(email=email)
                    if not var:
                        obj=Broker_info(fname=fname,lname=lname,address=address,city=city,
                        state=state,country=country,pincode=pincode,contact_number=long(contact_number),email=email,password=password,companyname=companyname)
                        obj.save()
                        String = utils.generate_string(size= 10)
                        number= random.randrange (10000,10000000 ,3)
                        temp=Broker_info.objects.get(email=email)
                        obj=verification(string=String,number=number,broker_id=temp)
                        obj.save();

                       # send_mail('Frieghttrackers', 'Actvate your account by clicking on link  here some link will come', 'from@example.com',
                       #['to@example.com'], fail_silently=False)

                        temp=Broker_info.objects.get(email=email)
                        request.session["uid"] =temp.id
                        return HttpResponseRedirect('/home/')
                    else:
                        return render(request,"registrationform.html",{"fname":fname,"lname":lname,"address":address,"city":city,
                        "state":state,"country":country,"pincode":pincode,"contact_number":long(contact_number),"email":email,"companyname":companyname,"error":error,"emailerror":"Email Already exist"})  
                  else:

                     return render(request,"registrationform.html",{"fname":fname,"lname":lname,"address":address,"city":city,"state":state,"country":country,"pincode":pincode,"contact_number":long(contact_number),"companyname":companyname,"email":email,"password":password,"error":error})    
                
    else:   
            return render(request,"registrationform.html")

def profile(request):
        try:    
          s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
          dic=s.get_decoded()
          b=Broker_info.objects.get(id=dic["uid"])
          print b.email_status
          print b.mobile_status
          if b.email_status and  b.mobile_status:
               email=b.email
               lat=24.585370
               lon=73.712275
               return  render(request,"profile.html",{"email":email,"lat":lat,"lon":lon})      
          else:
              return  HttpResponse("please verify your account")
        except:
              return HttpResponseRedirect('/home/')

def Addtruck(request):
          s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
          dic=s.get_decoded()
          b=Broker_info.objects.get(id=dic["uid"])
          if b.email_status=="TRUE" and  b.mobile_status=="TRUE":
               email=b.email
               render(request,"Addtruck.html",{"email":email})      
          else:
               HttpResponseRedirect("please verify your account")

def  home(request):
      
        if request.method=="POST":
          try:
            email=request.POST['email']
            password=request.POST['password']
            user=Broker_info.objects.get(email=email)
            if password == user.password:
                  request.session["uid"] =user.id
                  return HttpResponseRedirect('/profile/') 
          except:
              return render(request,"home.html",{"error":"some login error"})     
        else:
            return render(request,"home.html",{"error":""}) 
    

def logout(request):
      try:  
        s=Session.objects.get(session_key=request.COOKIES["sessionid"])
        s.delete()
        return HttpResponseRedirect("/home/")
      except:
        return HttpResponse("There might be some error whith logout")               
          

def Adddriver(request):
          s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
          dic=s.get_decoded()
          b=Broker_info.objects.get(id=dic["uid"])
          if b.email_status=="TRUE" and  b.mobile_status=="TRUE":
               email=b.email
               render(request,"Addtruck.html",{"email":email})      
          else:
               HttpResponseRedirect("please verify your account")            