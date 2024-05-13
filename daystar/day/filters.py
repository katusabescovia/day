# from django.utils import formats

# formatted_date = formats.date_format(receipt.date_sale, format="DATE_FORMAT")
import django_filters
from .models import *

class SitterFilter(django_filters.FilterSet):
    class Meta:
        model = Sitterform
        fields = ['name']



class Sitter_arrivalFilter(django_filters.FilterSet):
    class Meta:
        model = Sitter_arrival
        fields = ['sitter_name'] 



class Sitter_departureFilter(django_filters.FilterSet):
    class Meta:
        model = Sitter_departure
        fields = ['sitters_name']    


    
class Baby_Filter (django_filters.FilterSet):
    class Meta:
        model=Babiesform
        fields=['name_of_the_baby'] 


class payment_Filter(django_filters.FilterSet):
    class Meta:
        model = Payment
        fields = ['payee']     



class Departure_Filter(django_filters.FilterSet):
    class Meta:
        model = Departure
        fields = ['babys_name']   

class ProcurementFilter(django_filters.FilterSet):
    class Meta:
        model = Procurement
        fields = ['item_name']   

class SitterpaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Sitterpayment
        fields = ['sitter_name'] 

class DollFilter(django_filters.FilterSet):

    class Meta:
        model = Doll
        fields = ['name_of_the_doll']

