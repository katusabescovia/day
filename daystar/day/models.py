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
    babys_name=models.ForeignKey(Babiesform,on_delete=models.CASCADE)
    
    baby_number=models.IntegerField(default=0) 
    date=models.DateField(default=timezone.now)
    timeout=models.TimeField()
    pickers_name=models.CharField(max_length=200)
    comment=models.CharField(max_length=200,null=True, blank=True)
    def __str__(self):
        return self.babys_name
class  Payment(models.Model):
    payee = models.ForeignKey(Babiesform,on_delete=models.CASCADE ,null=True, blank=True)
    payment_type =models.CharField(choices=[('halfday', 'halfday'),('fullday', 'fullday'),('monthlyhalfday','monthlyhalfday') ,('monthlyfullfday','monthlyfullday')], max_length=100)
    payno = models.IntegerField(null=True, blank=True)
    actual_amount = models.IntegerField(default=0,)
    amount_paid = models.IntegerField(default=0)
    date=models.DateField(default=timezone.now)
    def __int__(self):
      return self.payee   
    
    def amount(self):
        halfday=10000
        fullday=15000
        amount=(self.payment_type['monthlyfullday']*30, self.payment_type['monthlyhalfday']*30)
        return int(amount)


    def get_balance(self):
        return self.actual_amount - self.amount_paid  

    
class Sitterform(models.Model):  
    name=models.CharField(max_length=200)
    gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=100)
    location=models.CharField(choices=[('kabalagala', 'kabalagala')], max_length=100)
    date_of_birth=models.DateField(default=timezone.now) 
    next_of_kin=models.CharField( max_length=200)
    national_identification_number=models.CharField(max_length=200)
    recommenders_name=models.CharField(max_length=200)
    religon=models.CharField(max_length=200,null=True, blank=True)
    level_of_education=models.CharField( choices=[('diploma','Diploma'),('highschool certificate','Highschool certificate'),('others','Others')],max_length=200)
    sitter_number=models.IntegerField(default=0)
    contacts=models.CharField(max_length=200) 
    date=models.DateField()
    def __str__(self):
        return self.name

class Sitter_arrival(models.Model):
    sitter_name=models.ForeignKey(Sitterform, on_delete=models.CASCADE) 
    sitter_number=models.IntegerField(default=0)
    date_of_arrival=models.DateField(default=timezone.now)   
    timein=models.TimeField ()
    Attendancestatus=models.CharField(choices=[('onduty', 'onduty')], max_length=100)
    def __str__(self):
        return str(self.sitter_name)
class Sitter_departure(models.Model):
    sitters_name=models.ForeignKey(Sitter_arrival, on_delete=models.CASCADE) 
    sitter_number=models.IntegerField(default=0)
    date_of_departure=models.DateField(default=timezone.now)   
    timeout=models.TimeField ()  
    def __str__(self):
       return self.sitters_name
   


class Arrival(models.Model):
    baby_name=models.ForeignKey(Babiesform, on_delete=models.CASCADE)
    baby_number=models.IntegerField(default=0)
    date=models.DateField(default=timezone.now)
    timein=models.TimeField()
    care_taker=models.CharField(max_length=200)
    Assigned_to=models.ForeignKey(Sitter_arrival,on_delete=models.CASCADE)

    def __str__(self):
        return self.baby_name    

class Category_doll(models.Model):  
    name = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name 
  
class Doll(models.Model):
    c_doll=models.ForeignKey(Category_doll, on_delete=models.CASCADE,null=True, blank=True)
    name_of_the_doll =models.CharField(max_length=200,null=True, blank=True)
    quantity=models.IntegerField(default=0)
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
    
class Procurement(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    item_name = models.CharField(max_length=200,)
    Quantity=models.IntegerField(default=0)
    date=models.DateField()
    Unit_price=models.IntegerField( null=True)
    received_quantity=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.item_name
      
class Usedlog(models.Model): 
    item = models.ForeignKey(Procurement,on_delete=models.CASCADE) 
    quantity_issued=models.IntegerField(default=0)
    usage_date=models.DateField()
    

class Sitterpayment(models.Model):
    sitter_name=models.ForeignKey(Sitterform, on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    date=models.DateField(default=timezone.now)
    numbers_of_babies_attended_to=models.IntegerField(default=0)
    def __str__(self):
        return f"Sitter Payment - {self.sitter_name}"


    def total_amount(self):
        total= self.amount * self.numbers_of_babies_attended_to
        return int(total)