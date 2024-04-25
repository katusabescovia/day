from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.forms import CharField, PasswordInput,TextInput,EmailField, PasswordInput

class BabiesformForm(ModelForm):
    class Meta:
        model = Babiesform
        fields = '__all__'
        widgets = {
            'name_of_the_baby': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'parents_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'babys_number': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'timein': forms.TimeInput(attrs={'class': 'form-control'}),
            'timeout': forms.TimeInput(attrs={'class': 'form-control'}),
            'c_stay': forms.Select(attrs={'class': 'form-control'}),
            'c_fees': forms.Select(attrs={'class': 'form-control'}),
            'name_of_the_person_brought_by_the_baby': forms.TextInput(attrs={'class': 'form-control'}),
            'name_of_the_person_that_taken_a_child': forms.TextInput(attrs={'class': 'form-control'}),}
        

class SitterformForm(ModelForm):
    class Meta:
        model = Sitterform
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'        
        
class SalesrecordForm(ModelForm):
    class Meta:
        model = Salesrecord
        fields = '__all__'
class  Doll(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__'

     
class ProcurementForm(ModelForm):
    class Meta:
        model = Procurement
        fields = '__all__'


