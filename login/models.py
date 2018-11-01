from django.db import models
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
	#mail=models.EmailField()
	pan=models.CharField(max_length=15)

class R1a(models.Model):
	gstinb=models.CharField(max_length=15)
	gstin=models.ForeignKey(Client,on_delete=models.CASCADE)
