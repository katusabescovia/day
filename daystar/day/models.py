from django.db import models
from django.utils import timezone

# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name

class Babiesform(models.Model):
    c_stay=models.ForeignKey(Categorystay ,on_delete=models.CASCADE,null=True, blank=True)
    name_of_the_baby=models.CharField(max_length=200, blank=True,null=True)
    gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=10, null=True, blank=True)
    age=models.IntegerField(default=0)
    parents_name=models.CharField(max_length=200,null=True, blank=True)
    care_taker=models.CharField(max_length=200)
    pickers_name=models.CharField(max_length=200,null=True, blank=True)
    location=models.CharField(max_length=50, null=True, blank=True)
    babys_number=models.IntegerField(default=0 ,null=True, blank=True)
    timein=models.TimeField(blank=True,null=True)
    timeout=models.TimeField(blank=True,null=True)
    date=models.DateField(default=timezone.now)
   


    def __str__(self):
        return self.name_of_the_baby
    

class  Payment(models.Model):
    payee = models.ForeignKey(Babiesform,on_delete=models.CASCADE ,null=True, blank=True)
    c_payment = models.ForeignKey(Categorystay, on_delete=models.CASCADE,null=True, blank=True) 
    amount=models.IntegerField(null=True, blank=True)
    payno = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10,null=True, blank=True,default='ugx')
    def __int__(self):
      return self.payee     
    
class Sitterform(models.Model):  
     name=models.CharField(max_length=200,null=True, blank=True)
     gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=10, null=True, blank=True)
     location=models.CharField(max_length=200,null=True, blank=True) 
     date_of_birth=models.DateField(null=True, blank=True) 
     next_of_kin=models.CharField( max_length=200,null=True, blank=True)
     national_identification_number=models.CharField(max_length=200,null=True, blank=True)
     recommenders_name=models.CharField(max_length=200,null=True, blank=True)
     religon=models.CharField(max_length=200,null=True,blank=True)
     level_of_education=models.CharField( choices=[('diploma','Diploma'),('highschool','Highschool'),('others','Others')],null=True, blank=True,max_length=200)
     sitter_number=models.IntegerField(default=0)
     contacts=models.CharField(max_length=200) 
     date=models.DateField(default=timezone.now)
     def __str__(self):
         return self.name
class Doll(models.Model):
    name=models.CharField(max_length=200,null=True, blank=True)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    category=models.CharField(max_length=200,null=True, blank=True)
    color=models.CharField(max_length=200, null=True,blank=True)
    size=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.name
class Salesrecord(models.Model):    
    doll=models.ForeignKey(Doll,  on_delete=models.CASCADE,null=True, blank=True)
    payee=models.ForeignKey(Babiesform, on_delete=models.CASCADE,null=True,blank=True)
    quantity_sold=models.IntegerField(default=0)
    total_price=models.IntegerField(default=0)
    sale_date=models.DateField(default=0)
    comments=models.CharField(max_length=100)
    total_cost=models.IntegerField(default=0)
    total_revenue=models.IntegerField(default=0)
    profitamount=models.IntegerField(default=0)
    def __str__(self):
        return self.doll.name
    
class  Procurement(models.Model):
    Item_CHOICES = (
        ('Diapers', 'Diapers'),
        ('Fruits', 'Fruits'),
        ('Milk', 'Milk'),
        ('Others', 'Others'),) 
    item_name = models.CharField(max_length=200, choices=Item_CHOICES, null=True, blank=True)
    Quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    date=models.DateField(auto_now_add=True, null=True)
    Unit_price=models.IntegerField( null=True)
    total_cost=models.IntegerField(default=0)
    net_stock=models.IntegerField(default=0)
    def __str__(self):
        return self.item_name








     
     
     
