from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class  Broker_info(models.Model):
    fname = models.CharField(max_length=30,blank=False)
    lname = models.CharField(max_length=30,blank=False)
    email=models.EmailField(blank=False,unique=True)
    city=models.CharField(max_length=30,blank=False)
    state=models.CharField(max_length=30,blank=True)
    contact_number=models.BigIntegerField(blank=False)
    password = models.CharField(max_length=50,blank=False)
    companyname=models.CharField(max_length=30,blank=False)
    rating=models.IntegerField(default=0,blank=False)
    email_status=models.BooleanField(default=True,blank=False)
    mobile_status=models.BooleanField(default=True,blank=False)
    lat=models.DecimalField(max_digits=12, decimal_places=9,blank=True)
    lon=models.DecimalField(max_digits=12, decimal_places=9,blank=True)
    updatelocation=models.BooleanField(default=False)


class verification(models.Model):
    string=models.CharField(max_length=50,blank=False)
    number=models.IntegerField(blank=False)
    broker_id=models.ForeignKey('Broker_info')

class truck_info(models.Model):
    state=models.CharField(max_length=2,blank=False)
    rto=models.CharField(max_length=3,blank=False)
    numberone=models.CharField(max_length=3,blank=True)
    numbertwo=models.IntegerField(max_length=4,blank=False)
    truck_type=models.CharField(max_length=30,blank=False)
    truck_model=models.CharField(max_length=30,blank=False)
    truck_tyre=models.IntegerField(max_length=4,blank=False)
    Capacity=models.IntegerField(max_length=10,blank=False)
    body_length=models.IntegerField(max_length=10,blank=False)
    body_width=models.IntegerField(max_length=10,blank=False)
    pref_item=models.CharField(max_length=30,blank=False)
    rc_book=models.FileField(upload_to='documents/rc/')
    puc_book=models.FileField(upload_to='documents/puc/')
    insurance_book=models.FileField(upload_to='documents/insurance/')
    driver=models.ForeignKey('driver_info')
    gps=models.ForeignKey('gps_info')
    broker=models.ForeignKey('Broker_info')
    verify=models.BooleanField(default=False,blank=False)

class driver_info(models.Model):
    fname=models.CharField(max_length=30,blank=False)
    lname=models.CharField(max_length=30,blank=False)
    address =models.CharField(max_length=30,blank=False)
    city=models.CharField(max_length=30,blank=False)
    state=models.CharField(max_length=30,blank=False)
    country=models.CharField(max_length=30,blank=False)
    pincode=models.IntegerField(blank=False,validators=[RegexValidator(regex='^.{6}$', message='Length has to be 6', code='nomatch')])
    contact_number=models.BigIntegerField(blank=False)
    license_number=models.CharField(max_length=30,blank=False)
    age=models.IntegerField(max_length=2,blank=False)
    broker=models.ForeignKey('Broker_info')
    
class gps_info(models.Model):    
    number=models.IntegerField(max_length=10,blank=False)
class gps_track(models.Model):
    gps=models.ForeignKey('gps_info')
    source_city=models.CharField(max_length=30,blank=False)
    source_state=models.CharField(max_length=30,blank=False)
    dest_city=models.CharField(max_length=30,blank=False)
    dest_state=models.CharField(max_length=30,blank=False)


class  load_info(models.Model):
    source = models.CharField(max_length=30,blank=False)
    destination = models.CharField(max_length=30,blank=False)
    pickupdate=models.DateField(blank=False)
    loadtype=models.CharField(max_length=30,blank=False)
    quantity=models.CharField(max_length=30,blank=False)
    numoftruck=models.IntegerField(blank=False)
    shipper=models.ForeignKey('Shipper_info')
    


class Shipper_info(models.Model):
    email=models.EmailField(blank=False,unique=True)
    password =models.CharField(max_length=30,blank=True)
    contact_number=models.BigIntegerField(blank=False)
    email_status=models.BooleanField(default=True,blank=False)
    lat=models.DecimalField(max_digits=12, decimal_places=9,blank=True)
    lon=models.DecimalField(max_digits=12, decimal_places=9,blank=True)
    updatelocation=models.BooleanField(default=False)
    companyname=models.CharField(blank=False,max_length=30)
    
class deal(models.Model):
    load_info=models.ForeignKey('load_info')
    Broker_info=models.ForeignKey('Broker_info')
    cost=models.IntegerField(blank=False)
    Shipper_info=models.ForeignKey('Shipper_info')       
       








    