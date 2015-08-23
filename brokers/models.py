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

    