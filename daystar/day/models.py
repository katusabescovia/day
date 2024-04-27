from django.db import models
from django.utils import timezone

# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name

class Babiesform(models.Model):
    c_stay=models.ForeignKey(Categorystay ,on_delete=models.CASCADE,default=1)
    name_of_the_baby=models.CharField(max_length=200, )
    gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=100)
    age=models.IntegerField(default=0)
    parents_name=models.CharField(max_length=200)
    location=models.CharField(max_length=50)
    babys_number=models.IntegerField(default=0 )
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name_of_the_baby

class Departure(models.Model):
    baby_name=models.ForeignKey(Babiesform,on_delete=models.CASCADE)
    
    baby_number=models.IntegerField(default=0) 
    date=models.DateField(default=timezone.now)
    timeout=models.TimeField()
    pickers_name=models.CharField(max_length=200)
    comment=models.CharField(max_length=200,null=True, blank=True)
    def __str__(self):
        return self.baby_number
class Arrival(models.Model):
    baby_name=models.ForeignKey(Babiesform, on_delete=models.CASCADE)
    baby_number=models.IntegerField(default=0)
    date=models.DateField(default=timezone.now)
    timein=models.TimeField()
    care_taker=models.CharField(max_length=200)

    def __str__(self):
        return self.baby_number



   
    

class  Payment(models.Model):
    payee = models.ForeignKey(Babiesform,on_delete=models.CASCADE ,null=True, blank=True)
    c_payment = models.ForeignKey(Categorystay, on_delete=models.CASCADE,null=True, blank=True) 
    amount=models.IntegerField(null=True, blank=True)
    payno = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10,null=True, blank=True,default='ugx')
    def __int__(self):
      return self.payee     
    
class Sitterform(models.Model):  
     name=models.CharField(max_length=200)
     gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=100)
     location=models.CharField(max_length=100) 
     date_of_birth=models.DateField(default=timezone.now) 
     next_of_kin=models.CharField( max_length=200)
     national_identification_number=models.CharField(max_length=200)
     recommenders_name=models.CharField(max_length=200)
     religon=models.CharField(max_length=200)
     level_of_education=models.CharField( choices=[('diploma','Diploma'),('highschool certificate','Highschool certificate'),('others','Others')],max_length=200)
     sitter_number=models.IntegerField(default=0)
     contacts=models.CharField(max_length=200) 
     date=models.DateField()
     def __str__(self):
         return self.name

class Sitter_arrival(models.Model):
     sitter_name=models.ForeignKey(Sitterform, on_delete=models.CASCADE) 
     sitter_number=models.IntegerField(default=0)
     date_of_arrival=models.DateField() 
     date=models.DateField(default=timezone.now)  
     timein=models.TimeField ()
     Attendancestatus=models.CharField(max_length=100)
     def __str__(self):
         return self.sitter_name
     
    
class Category_doll(models.Model):  
     name = models.CharField(max_length=100,null=True, blank=True)
     def __str__(self):
         return self.name   
class Doll(models.Model):
    c_doll=models.ForeignKey(Category_doll, on_delete=models.CASCADE,null=True, blank=True)
    name_of_the_doll =models.CharField(max_length=200,null=True, blank=True)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    category=models.CharField(max_length=200,null=True, blank=True)
    color=models.CharField(max_length=200, null=True,blank=True)
    size=models.CharField(max_length=200,null=True,blank=True)
    issued_quantity=models.IntegerField(default=0,blank=True,null=True) 
    received_quantity=models.IntegerField(default=0,null=True,blank=True)
    Unit_price=models.IntegerField(default=0,null=True, blank=True)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name_of_the_doll
class Salesrecord(models.Model):    
    doll=models.ForeignKey(Doll,  on_delete=models.CASCADE,null=False, blank=False)
    payee=models.ForeignKey(Babiesform, on_delete=models.CASCADE,null=False,blank=False)
    quantity_sold=models.IntegerField(default=0)
    amount_received=models.IntegerField(default=0)
    sale_date=models.DateField(default=timezone.now)
    unit_price=models.IntegerField(default=0)
     


     
    
    def get_total(self):
        total= self.quantity_sold * self.unit_price
        return int( total)
#here we are getting change.(money to be given to theparent)    
    def get_change(self):
        change= self.get_total() - self.amount_received
        return int(change)#sales is linked to products
    
    

class Category(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True) 
    def __str__(self):
        return self.name 
    
class  Procurement(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    item_name = models.CharField(max_length=200,)
    Quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    date=models.DateField(auto_now_add=True, null=True)
    Unit_price=models.IntegerField( null=True)
    total_cost=models.IntegerField(default=0)
    net_stock=models.IntegerField(default=0)

    def __str__(self):
        return self.item_name








     
     
     
