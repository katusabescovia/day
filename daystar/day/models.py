from django.db import models
from django.utils import timezone

# Create your models here.
class Category_stay(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name

class Babiesform(models.Model):
    c_stay=models.ForeignKey(Category_stay ,on_delete=models.CASCADE,null=True, blank=True)
    name_of_the_baby=models.CharField(max_length=200, blank=True,null=True)
    gender=models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=10, null=True, blank=True)
    age=models.IntegerField(default=0)
    parents_name=models.CharField(max_length=200,null=True, blank=True)
    name_of_the_person_brought_by_the_baby=models.CharField(max_length=200)
    name_of_the_person_that_has_taken_a_child=models.CharField(max_length=200,null=True, blank=True)
    location=models.CharField(max_length=50, null=True, blank=True)
    babys_number=models.IntegerField(default=0 ,null=True, blank=True)
    comment=models.TextField(blank=True,null=True )
    timein=models.TimeField(blank=True,null=True)
    timeout=models.TimeField(blank=True,null=True)
    date=models.DateField(default=timezone.now)


    def __str__(self):
        return self.name_of_the_baby
    

class  Payment(models.Model):
    payee = models.ForeignKey(Babiesform,on_delete=models.CASCADE ,null=True, blank=True)
    c_payment = models.ForeignKey(Category_stay, on_delete=models.CASCADE,null=True, blank=True) 
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
     
     
