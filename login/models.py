from django.db import models
from django.db.models import IntegerField
#from phone_field import PhoneField

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

<<<<<<< HEAD

class R1b(models.Model):
    gstin = models.ForeignKey(Client, on_delete=models.CASCADE)
    gstinb = models.CharField(max_length=15,)
    quarter = models.CharField(max_length=20)
    nil_supply_is = models.IntegerField()
    nil_supply_ws = models.IntegerField()
    non_gst_is = models.IntegerField()
    non_gst_ws = models.IntegerField()
    other_exempted_is = models.IntegerField()
    other_exempted_ws = models.IntegerField()


class Client_extra(models.Model):
    gstin = models.ForeignKey(Client, on_delete=models.CASCADE)
    house_no = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    pincode = models.IntegerField()
    adhaar = models.CharField(max_length=20)


class B3a(models.Model):
    gstin = models.ForeignKey(Client, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    intypeb3a = models.CharField(max_length=20)
    total_taxable_value = models.IntegerField()


class R2a(models.Model):
    gstin = models.ForeignKey(Client, on_delete=models.CASCADE)
    intyper2a = models.CharField(max_length=4)
    invoice_no = models.IntegerField()
    invoice_date = models.DateField
    invoice_value = models.IntegerField()
    tax_rate = models.IntegerField()
    taxable_value = models.IntegerField()
    total_taxable_value = models.IntegerField()
    igst = models.IntegerField()
    cgst = models.CharField(max_length=20)
    sgst = models.IntegerField()
    cess = models.IntegerField()
    month = models.CharField(max_length=20)
class B3b(models.Model):
    gstin = models.ForeignKey(Client, on_delete=models.CASCADE)
    intypeb3b = models.CharField(max_length=4)
    total_taxable_value = models.IntegerField()
    igst = models.IntegerField()
    cgst = models.CharField(max_length=20)
    sgst = models.IntegerField()
    cess = models.IntegerField()
    month = models.CharField(max_length=20)
=======
class R1b(models.Model):
	gstinb=models.charField(max_length=15,primary_key=True)
	quarter=models.CharField(max_length=20)
	nil_supply_is=models.IntegerField()
	nil_supply_w=models.IntegerField()
	non_gst_is=models.IntegerField()
	non_gst_ws=models.IntegerField()
	other_exempted_is=models.IntegerField()
	other_exempted_ws=models.IntegerField()

class Client_extra(models.Model):
	house_no=models.charfield(max_length=20)
	street=models.CharField(max_length=20)
	area=models.charfield(max_length=20)
	city=models.charfield(max_length=20)
	district=models.charfield(max_length=20)
	pincode=models.IntegerField()
	adhaar=models.charfield(max_length=20)

class B3a(object):
	monthly=models.charfield(max_length=20)
	state=models.charfield(max_length=20)
	intype=models.charfield(max_length=20)
	total_taxablevalue=models.IntegerField()
	
class R2a
	intype=models.charfield(max_length=20)
	invoice_no=models.IntegerField() 
	invoice_date=models.DateField
	invoice_value=models.IntegerField()
	tax_rate=models.IntegerField()
	taxable_value=models.IntegerField()
	total_taxablevalue=models.IntegerField()
	igst=models.IntegerField()
	cgst=models.charfield(max_length=20)
	sgst=models.IntegerField()
	cess=models.IntegerField()
	monthly=models.charfield(max_length=20);
>>>>>>> 4d4efe7cce9c896ed5f0910004af1318ebe0968c
