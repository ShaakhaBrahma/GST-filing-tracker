from django.db import models
from django.db.models import IntegerField
from phone_field import PhoneField

# Create your models here.
#class Animal(models.Model):
#	name=models.CharField(max_length=10,primary_key=True)
#	age=models.IntegerField()
	#spouse=models.ForeignKeyField(animal)
class Client(models.Model):
	gstin=models.CharField(max_length=15,primary_key=True)
	name=models.CharField(max_length=20)
	phn=models.CharField(max_length=11)
	usr=models.CharField(max_length=10)
	passwd=models.CharField(max_length=15)
	mail=models.CharField(max_length=15)
	pan=models.CharField(max_length=15)

class R1a(models.Model):
	gstin=models.ForeignKey(Client,on_delete=models.CASCADE)
	gstinb=models.CharField(max_length=15)
	month=models.CharField(max_length=8)
	invoice_no=models.IntegerField()
	cust_name=models.CharField(max_length=20)
	state_of_supply=models.CharField(max_length=15)
	invoice_date=models.DateField()
	invoice_value=models.IntegerField()
	tax_rate=models.IntegerField()
	taxable_value: IntegerField=models.IntegerField()
	cgst=models.IntegerField()
	sgst=models.IntegerField()
	igst=models.IntegerField()
	cess=models.IntegerField()
