from django.db import models
# from phone_field import PhoneField

# Create your models here.
# class Animal(models.Model):
#	name=models.CharField(max_length=10,primary_key=True)
#	age=models.IntegerField()
# spouse=models.ForeignKeyField(animal)
class Client(models.Model):
    gstin = models.CharField(max_length=15, primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    phn = models.CharField(max_length=11)
    usr = models.CharField(max_length=10)
    passwd = models.CharField(max_length=15)
    mail = models.CharField(max_length=15)
    pan = models.CharField(max_length=15)
    provisional_id = models.CharField(max_length=15)

class R1a(models.Model):
    gstin = models.ForeignKey(Client, on_delete=models.CASCADE)
   # gstinb = models.CharField(max_length=15)
    month = models.CharField(max_length=8)
   # invoice_no = models.IntegerField()
   # cust_name = models.CharField(max_length=20)
   # state_of_supply = models.CharField(max_length=15)
   # invoice_date = models.DateField()
   # invoice_value = models.IntegerField()
   # tax_rate = models.IntegerField()
    taxable_value = models.IntegerField()
    cgst = models.IntegerField(null=True)
    sgst = models.IntegerField(null=True)
    igst = models.IntegerField(null=True)
    cess = models.IntegerField(null=True)
    total = models.IntegerField(null=True)


class R1b(models.Model):
    gstin = models.ForeignKey(Client, on_delete=models.CASCADE)
    #gstinb = models.CharField(max_length=15, )
    month = models.CharField(max_length=20)
    nil_supply_is = models.IntegerField(null=True)
    nil_supply_ws = models.IntegerField(null=True)
    non_gst_is = models.IntegerField(null=True)
    non_gst_ws = models.IntegerField(null=True)
    other_exempted_is = models.IntegerField(null=True)
    other_exempted_ws = models.IntegerField(null=True)
    total = models.IntegerField(null=True)


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
    #state = models.CharField(max_length=20)
    ty = models.CharField(max_length=3)
    taxable_value = models.IntegerField()
    total = models.IntegerField()
    igst = models.IntegerField()



class R2a(models.Model):
    gstin = models.ForeignKey(Client, on_delete=models.CASCADE)
    #intyper2a = models.CharField(max_length=4)
    #invoice_no = models.IntegerField()
    #invoice_date = models.DateField
    #invoice_value = models.IntegerField()
    #tax_rate = models.IntegerField()
    taxable_value = models.IntegerField()
    total = models.IntegerField()
    igst = models.IntegerField(null=True)
    cgst = models.IntegerField(null=True)
    sgst = models.IntegerField(null=True)
    cess = models.IntegerField(null=True)
    month = models.CharField(max_length=20)


class B3b(models.Model):
    gstin = models.ForeignKey(Client, on_delete=models.CASCADE)
    #intypeb3b = models.CharField(max_length=4)
    taxable_value = models.IntegerField()
    igst = models.IntegerField(null=True)
    cgst = models.IntegerField(null=True)
    sgst = models.IntegerField(null=True)
    cess = models.IntegerField(null=True)
    month = models.CharField(max_length=20)
    ty = models.CharField(max_length=3)
    total = models.IntegerField()
