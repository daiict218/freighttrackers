from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class  Broker_info(models.Model):
    fname = models.CharField(max_length=30,blank=False)
    lname = models.CharField(max_length=30,blank=False)
    email=models.EmailField(blank=False,unique=True)
    address =models.CharField(max_length=30,blank=False)
    city=models.CharField(max_length=30,blank=False)
    state=models.CharField(max_length=30,blank=False)
    country=models.CharField(max_length=30,blank=False)
    pincode=models.IntegerField(blank=False,validators=[RegexValidator(regex='^.{6}$', message='Length has to be 6', code='nomatch')])
    contact_number=models.BigIntegerField(blank=False)
    password = models.CharField(max_length=50,blank=False)
    companyname=models.CharField(max_length=30,blank=False)
    rating=models.IntegerField(default=0,blank=False)
    email_status=models.BooleanField(default=True,blank=False)
    mobile_status=models.BooleanField(default=True,blank=False)


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
    num_tyre=models.IntegerField(max_length=4,blank=False)
    Capacity=models.IntegerField(max_length=10,blank=False)
    body_length=models.IntegerField(max_length=10,blank=False)
    body_width=models.IntegerField(max_length=10,blank=False)
    pref_item=models.CharField(max_length=30,blank=False)
    rc_book=models.FileField(upload_to='documents/')
    puc_book=models.FileField(upload_to='documents/')
    insurance_book=models.FileField(upload_to='documents/')
    driver=models.ForeignKey('driver_info')
    gps=models.ForeignKey('gps_info')

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
 
class gps_info(models.Model):    
    number=models.IntegerField(max_length=10,blank=False)









    