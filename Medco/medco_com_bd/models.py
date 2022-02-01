from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


# City choice
STATE_CHOICES=(
    ("Barisal","Barisal"),
    ("Dhaka North","Dhaka North"),
     ("Dhaka South","Dhaka South")
      
) 


class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    number=models.IntegerField()
    locality=models.CharField(max_length=100)
    city=models.CharField(choices=STATE_CHOICES,max_length=50)


    def __str__(self):
        return str(self.id)



# produdct choice
CATAGORY_CHOICES=(
    ("BABY","Baby Product"),
    ("FEMALE","Female product"),
    ("MALE","Male product"),
    ("SEX","Sexual product")
)

class Product(models.Model):
    titel=models.CharField(max_length=100,blank=True)
    small_name=models.CharField(max_length=100,blank=True)
    generic_name=models.CharField(max_length=200,blank=True)
    strength=models.CharField(max_length=20,blank=True)
    manufactured_by=models.CharField(max_length=50,blank=True)
    unit_price=models.FloatField()
    pack_price=models.CharField(max_length=100,blank=True)
    indications=models.CharField(max_length=500,blank=True)
    therapeutic_class=models.CharField(max_length=500,blank=True)
    pharmacology=models.CharField(max_length=500,blank=True)
    dosag_and_administration=models.CharField(max_length=700,blank=True)
    interaction=models.CharField(max_length=500,blank=True)
    contraindications=models.CharField(max_length=500,blank=True)
    side_effects=models.CharField(max_length=500,blank=True)
    pregnancy_and_lactation=models.CharField(max_length=500,blank=True)
    precautions_and_warnings=models.CharField(max_length=500,blank=True)
    overdose_effects=models.CharField(max_length=500,blank=True,null=True)
    storage_conditions=models.CharField(max_length=500,blank=True)
    Catagory=models.CharField(choices=CATAGORY_CHOICES,max_length=20,blank=True)
    product_image=models.ImageField(upload_to="productimg",blank=True)
    

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity*self.product.unit_price

STATUS_CHOICES=(

    ("pending","pending"),
    ("accepted","accepted"),
    ("cancel","cancel"),
    ("prepairing","prepairing"),
    ("on the way","on the way"),
    ("delivered","delivered")
)
class Status(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    order_date_no_time=models.DateField(auto_now_add=True,null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    status=models.CharField(choices=STATUS_CHOICES,max_length=20,default="pending")


    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity*self.product.unit_price







class UserOtp(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time_st=models.DateTimeField(auto_now=True)
    otp=models.SmallIntegerField()

    def __str__(self):
        return str(self.id)










