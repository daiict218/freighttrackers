from django.shortcuts import render
from brokers.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.sessions.models import Session
from brokers import utils
from django.core.mail import send_mail

from uploadform import uploadform
import random
import urllib2
import json

# Create your views here.
def home(request):
    if request.method=='POST' and 'signup' in  request.POST:
                  print request
                  fname=request.POST['fname']
                  lname=request.POST['lname']
                  #address=request.POST['address']
                  #city=request.POST['city']
                  state=request.POST['state']
                  #country=request.POST['country']
                  pincode=request.POST['pincode']
                  contact_number=request.POST['contact_number']
                  email=request.POST['email']
                  companyname=request.POST['company']
                  password=request.POST['password']
                  crpassword=request.POST['crpassword']
                  pincode,pincode_error=utils.verify_pincode(pincode)
                  contact_number,cont_error=utils.verify_mobile(contact_number)
                  email,email_error=utils.verify_email(email)
                  pwd,pwd_error=utils.verify_passwords(password,crpassword)
                  calender=myform()
                  error=[]
                  if fname=='':
                       error.append("first name is required")
                  if lname=='':
                       error.append("last name is required")
                  # if address=='':
                  #      error.append("address  is required")
                  # if city=='':
                  #      error.append("city is required")
                  if  state=='':
                        error.append("state is required")
                  if companyname=='':
                       error.append("company name is required")                         
                  if pincode=='-1':
                       pincode=''
                       error.append(pincode_error)
                  else:
                       print pincode
                       pincode=int(pincode)
                       response1 = urllib2.urlopen('https://www.WhizAPI.com/api/v2/util/ui/in/indian-city-by-postal-code?AppKey=nwbht9wqibmyynjlv3xezyer&pin=%d' %pincode)
                       try:
                         temp=json.load(response1)
                         #print temp
                         list_city=temp["Data"]
                         #print " /n"
                         print list_city
                         dic=list_city[0]
                         #print dic
                        

                         city=dic['City']
                         #print city
                         country=dic['Country']
                         #print country
                         address=''

                         #state=''
                         
                       except: 
                         error.append("Enter valid pincode")
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
                        
                        return HttpResponseRedirect('/profile/')
                    else:
                        return render(request,"home.html",{"fname":fname,"lname":lname,"pincode":pincode,"contact_number":contact_number,"email":email,"companyname":companyname,"error":error,"emailerror":"Email Already exist"})  
                  else:

                     return render(request,"home.html",{"fname":fname,"lname":lname,"pincode":pincode,"contact_number":contact_number,"companyname":companyname,"email":email,"password":password,"error":error})    
                
    elif request.method=="POST" and 'login' in request.POST:
                  try:
                    email=request.POST['email']
                    password=request.POST['password']
                    user=Broker_info.objects.get(email=email)
                    if password == user.password:
                        request.session["uid"] =user.id
                        return HttpResponseRedirect('/profile/')
                    else:
                        return HttpResponseRedirect('/home/')     
                  except:
                      return render(request,"home.html",{"error":"some login error"})

    elif request.method=="POST" and 'shipperlogin' in request.POST:
                  try:
                    email=request.POST['shipperemail']
                    password=request.POST['shipperpassword']
                    user=Shipper_info.objects.get(email=email)
                    if password == user.password:
                        request.session["uid"] =user.id
                        return HttpResponseRedirect('/shipperprofile/')
                    else:
                        return render(request,"home.html",{"error":"Wrong Password"})     
                  except:
                      return render(request,"home.html",{"error":"some login error"}) 
    elif request.method=='POST' and 'query' in request.POST:
                  source = request.GET['source']
                  destination = request.GET['destination']
                  pickupdate=request.GET['pickupdate']
                  loadtype=request.GET['loadtype']
                  quantity=request.GET['quantity']
                  numoftruck=request.GET['numoftruck']
                  email=request.GET['email']
                  password =request.GET['password']
                  contact_number=request.GET['contact_number']
                  try:
                        temp=Shipper_info.objects.get(email=email)
                        obj=load_info(source=source,destination=destination,pickupdate=pickupdate,
                        loadtype=loadtype,quantity=quantity,numoftruck=numoftruck,shipper=temp)
                        obj.save()
                        return render(request,"home.html",{"error":"Shipper already have account please login by that acccount"})   
                  except:
                        obj=Shipper_info(email=email,password=password,contact_number=contact_number)
                        obj.save()
                        temp=Shipper_info.objects.get(email=email)              
                        obj=load_info(source=source,destination=destination,pickupdate=pickupdate,
                        loadtype=loadtype,quantity=quantity,numoftruck=numoftruck,shipper=temp)
                        obj.save()
                        return HttpResponseRedirect('/shipperprofile/')
                                                                      
    else:    
            return render(request,"home.html")

def profile(request):
  if request.method=="POST":
         cost=request.POST['cost']
         loadid=int(request.POST['request'])
         print loadid
         s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
         dic=s.get_decoded()
         b=Broker_info.objects.get(id=  dic["uid"])
         l=load_info.objects.get(id=loadid)
         shipper=Shipper_info.objects.get(id=l.shipper_id)
         obj=deal(cost=cost,load_info=l,Broker_info=b,Shipper_info=shipper)
         obj.save()
         print "hello"
         return HttpResponseRedirect("/profile/")
  else:  
        try: 
            
          s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
          dic=s.get_decoded()
          b=Broker_info.objects.get(id=dic["uid"])
          if b.email_status and  b.mobile_status:
              email=b.email
              address=b.address
              city=b.city
              state=b.state
              country=b.country
               #print 'https://api.mapmyindia.com/v3?fun=geocode&lic_key=316sy79cku9swmmmqc7brq6gapznn8s2&q=%s,%s' %(city,state)
               
               #try:
               #   response1 = urllib2.urlopen('https://api.mapmyindia.com/v3?fun=geocode&lic_key=316sy79cku9swmmmqc7brq6gapznn8s2&q=%s,%s' %(city,state))
               #   temp=json.load(response1)
               #    print temp
               #    dic=temp[0]
               #    lat=dic['lat']
               #    lon=dic['lng']          
                         
               # except: 
              lat=28.613939
              lon=77.209021

              resultset=load_info.objects.all()
              loadlist=list(resultset)       
                        
              return  render(request,"profile.html",{"email":email,"lat":lat,"loadlist":loadlist,"lon":lon})      
          else:
              return  HttpResponse("please verify your account")
        except:
              return HttpResponseRedirect('/home/')

def Addtruck(request):
    if request.method=='GET':
        try:
            s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
        except:
            return HttpResponseRedirect('/home/')

        dic=s.get_decoded()
        b=Broker_info.objects.get(id=dic["uid"])
        if b.email_status and  b.mobile_status:
                email=b.email
                resultset=driver_info.objects.filter(broker_id=b.id)
                driver_list=list(resultset)
                return  render(request,"Addtruck.html",{"email":email,"driver_list":driver_list})      
                   
        else:
          return  HttpResponse("please verify your account")



def logout(request):
      try:  
        s=Session.objects.get(session_key=request.COOKIES["sessionid"])
        s.delete()
        return HttpResponseRedirect("/home/")
      except:
        return HttpResponse("There might be some error whith logout")               
          

def Adddriver(request):
    try:
          s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
    except:
          return HttpResponseRedirect('/home/')
    dic=s.get_decoded()
    b=Broker_info.objects.get(id=dic["uid"])
    if request.method=="GET":
        if b.email_status and  b.mobile_status:
           email=b.email
           return render(request,"Adddriver.html",{"email":email})      
        else:
           return HttpResponse("please verify your account") 

    else:
        dic=utils.verify_driver(request)  
        if not dic['error']:
            obj=driver_info(broker=b,fname=dic['fname'],license_number=dic['license_number'],lname=dic['lname'],address=dic['address'],city=dic['city'],
            state=dic['state'],country=dic['country'],pincode=dic['pincode'],contact_number=dic['contact_number'],age=dic['age'])
            obj.save()
            return HttpResponseRedirect('/managedriver/')
                        
        else:
            return render(request,"Adddriver.html",{"fname":dic['fname'],"lname":dic['lname'],"address":dic['address'],"city":dic['city'],
            "state":dic['state'] ,"licensenumber":dic['license_number'],"country":dic['country'],"pincode":dic['pincode'],"contact_number":dic['contact_number'],"error":dic['error']})  

def managedriver(request):                  
    try:
          s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
    except:
          return HttpResponseRedirect('/home/')
    dic=s.get_decoded()
    
    resultset=driver_info.objects.filter(broker=dic["uid"])
    driver_set=list(resultset)
    return render(request,"managedriver.html",{"driver_set":driver_set}) 


def managetruck(request):
 try:
      s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
 except:
      return HttpResponseRedirect('/home/')
 dic=s.get_decoded() 
 if  request.method=="GET":                  
    
    email=Broker_info.objects.get(id=dic["uid"]).email
    result_set=truck_info.objects.filter(broker=dic["uid"] , verify="True")
    truck_set=list(result_set)
    print truck_set
    place=[]
    i=0
    for item in truck_set:
        temp=gps_track.objects.get(gps=item.gps)
        place.append((truck_set[i],temp.source_city,temp.source_state,temp.dest_city,temp.dest_state))
        i=i+1
    print place    

    return render(request,"managetruck.html",{"email":email,"place":place})
 else:
    name=request.POST['driver']
    l=name.split(' ', 1 )
    fname=l[0]
    lname=l[1]
    driver=driver_info.objects.get(fname=fname,lname=lname,broker_id=dic["uid"])
    broker=Broker_info.objects.get(id=dic["uid"])
    gps=gps_info(id="1")
    state=request.POST['state']
    rto=request.POST['rto']
    numberone=request.POST['numberone']
    numbertwo=request.POST['numbertwo']
    truck_type=request.POST['type']
    truck_tyre=request.POST['tyre']
    truck_model=request.POST['model']
    Capacity=request.POST['capacity']
    body_length=request.POST['length']
    body_width=request.POST['width']
    pref_item=request.POST['item']
    puc_book=request.POST['puc']
    insurance_book=request.POST['insurance']
    rc_book=request.POST['rc']
    obj=truck_info(state=state,rto=rto,numberone=numberone,numbertwo=numbertwo,truck_type
        =truck_type,truck_tyre=truck_tyre,truck_model=truck_model,body_width=body_width,
        body_length=body_length,Capacity=Capacity,pref_item=pref_item,puc_book=puc_book,
        rc_book=rc_book,insurance_book=insurance_book,gps=gps,driver=driver,broker=broker)
    obj.save()

    return HttpResponseRedirect("/profile/") 


def shipperProfile(request):
    if request.method=="GET":
            s=Session.objects.get(session_key=request.COOKIES["sessionid"])    
            dic=s.get_decoded()
            b=Shipper_info.objects.get(id= dic["uid"])
            email=b.email
            resultset=deal.objects.filter(Shipper_info=dic["uid"])
            list_deal=list(resultset)
            lst=[]
            
            for item in list_deal:
                  send={}
                  load=item.load_info_id
                  s=load_info.objects.get(id=load)
                  b=item.Broker_info_id
                  broker=Broker_info.objects.get(id=b)
                  send={"id":item.id,"source":s.source,"destination":s.destination,"pickupdate":s.pickupdate,"loadtype":s.loadtype,
                  "quantity":s.quantity,"numoftruck":int(s.numoftruck),"cost":item.cost,"companyname":broker.companyname}
                  lst.append(send)
            print lst 
            lat=28.613939
            lon=77.209021         
                    
            return render(request,'shipperprofile.html',{"email":email,"lst":lst,"lat":lat,"lon":lon})
        

    
           



 
