from django.forms import ModelForm
from .models import *
from django import forms
from .models import Doll
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.forms import CharField, PasswordInput,TextInput,EmailField, PasswordInput

class BabiesformForm(ModelForm):
    class Meta:
        model = Babiesform
        fields = '__all__'
      
           
        

class SitterformForm(ModelForm):
    class Meta:
        model = Sitterform
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'        
        

class  DollForm(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__'

class Addform(ModelForm):
    class Meta:
        model = Doll
        fields = ['received_quantity']


     
class ProcurementForm(ModelForm):
    class Meta:
        model = Procurement
        fields = '__all__'


class SalesrecordForm(ModelForm):
    class Meta:
        model = Salesrecord
        fields = [ 'quantity_sold', 'amount_received', 'payee']  


# class ArrivalForm(ModelForm):
#      class Meta:
#          model=Arrival
#          fields='__all__'


class   DepartureForm(ModelForm):
     class Meta:
         model=Departure
         fields='__all__'

class Sitter_arrivalForm(ModelForm):
     class Meta:
         model=Sitter_arrival
         fields='__all__'

class AddForm(ModelForm):
     class Meta:
         model=Procurement
         fields=['received_quantity']  



class Usedlogform(ModelForm):
     class Meta:
         model=Usedlog
         fields='__all__'
class Add_form(ModelForm):
     class Meta:
         model=Procurement
         fields=['category', 'item_name','Quantity', 'Unit_price','date' ]
       
         


class SitterpaymentForm(ModelForm):
     class Meta:
         model=Sitterpayment
         fields='__all__'

     def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['amount'].disabled = True

class Sitter_departureform(ModelForm):
     class Meta:
      model=Sitter_departure
      fields='__all__'   




class Address_form(ModelForm):
     class Meta:
         model=Doll  
         fields=['c_doll','name_of_the_doll','quantity','color','size','date','Unit_price',]



   




