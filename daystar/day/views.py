from django.shortcuts import render,redirect,get_object_or_404
from django .contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from .forms import *
from .models import *
from django.contrib.postgres.search import SearchQuery, SearchVector
from . filters import *

# from .forms import BabiesformForm
# from .models import Babiesfor


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
@login_required
def home(request):
    return render(request,'home.html')

def logout(request):
    return render(request,'logout.html')
@login_required
def sitterpayment(request):
    return render(request,'sitterpayment.html')
@login_required
def babiesform(request):
    babies= Babiesform.objects.all()
    return render(request,'babiesform.html',{'babies':babies})
    
@login_required
def add(request):
    if request.method=='POST':
        form=BabiesformForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('babiesform')
    else:
        form=BabiesformForm()
    return render(request,'add.html',{'form':form})
    
        
@login_required
def read(request,id):
   babies_info=Babiesform.objects.get(id=id)
   return render(request,'read.html',{'babies_info':babies_info})
@login_required
def edit(request,id):
    baby=get_object_or_404(Babiesform,id=id)
    if request.method == 'POST':
       form=BabiesformForm (request.POST,instance=baby)
       if form.is_valid():
           form.save()
           return redirect('babiesform')
    else:
        form=BabiesformForm(instance=baby)
    return render(request,'edit.html',{'form':form,'baby':baby})       
        
    

@login_required
def sitterform(request):
    sitters=Sitterform.objects.all()
    return render(request,'sitterform.html',{'sitters':sitters})
    


@login_required
def adds(request):
    if request.method=='POST':
        form=SitterformForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('sitterform')
    else:
        form=SitterformForm()
    return render(request,'adds.html',{'form':form })         

    
@login_required
def reads(request,id):
    sitters_info=Sitterform.objects.get(id=id)
    return render(request,'reads.html',{'sitters_info':sitters_info})
    



@login_required
def edits(request,id):
    sitter=get_object_or_404(Sitterform,id=id)
    if request.method == 'POST':
       form=SitterformForm (request.POST,instance=sitter)
       if form.is_valid():
           form.save()
           return redirect('sitterform')
    else:
        form=SitterformForm(instance=sitter)
    return render(request,'edits.html',{'form':form,'sitter':sitter})     

def paymentform(request):
    payment= Payment.objects.all()
    return render(request,'paymentform.html',{'payment':payment})
    

def addpay(request):
    if request.method=='POST':
        form=PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('paymentform')
    else:
        form=PaymentForm()
    return render(request,'addpay.html',{'form':form})
    
        

def readpay(request,id):
   payment_info=Payment.objects.get(id=id)
   return render(request,'readpay.html',{'payment_info':payment_info})


def editpay(request,id):
    baby=get_object_or_404(Payment,id=id)
    if request.method == 'POST':
       form=PaymentForm(request.POST,instance=baby)
       if form.is_valid():
           form.save()
           return redirect('paymentform')
    else:
        form=PaymentForm(instance=baby)
    return render(request,'editpay.html',{'form':form,'baby':baby})  
 
def dollscorner(request, doll_id):
    doll = get_object_or_404(Doll, id=doll_id)
    return render(request, 'dollscorner.html', {'doll': doll})

@login_required
def receipt(request):
    sales= Salesrecord.objects.all().order_by('-id') 
    return render(request,'receipt.html',{'sales':sales})  
@login_required
def issue_item(request,pk):
    issued_item=Doll.objects.get(id=pk) 
    sales_form=SalesrecordForm(request.POST)  

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale=sales_form.save(commit=False)
            new_sale.doll=issued_item
            new_sale.unit_price=issued_item.Unit_price
            new_sale.save()
            issued_quantity=int(request.POST['quantity_sold'])
            issued_item.quantity-=issued_quantity
            issued_item.save()
            print(issued_item.name_of_the_doll)
            print(request.POST['quantity_sold'])
            print(issued_item.quantity)
            return redirect('receipt')
    return render(request, 'issue_item.html',{'sales_form':sales_form} )

@login_required
def receipt_detail(request, receipt_id):
            receipt = Salesrecord.objects.get(id=receipt_id)
            return render(request,'receipt_detail.html',{'receipt':receipt})

@login_required
def add_to_stock(request,pk):
    issued_item=Doll.objects.get(id=pk)
    form=Addform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            added_quantity=int(request.POST['received_quantity'])
            issued_item.quantity+=added_quantity
            issued_item.save()
            print(added_quantity)
            print(issued_item.quantity)
            return redirect('doll')
    return render(request, 'add_to_stock.html',{'form':form})

@login_required
def all_sales(request):
    sales=Salesrecord.objects.all()
    total=sum([items.amount_received for items in sales])
    change=sum([items.get_change() for items in sales])
    net=total-change
    return render(request,'all_sales.html',{'sales':sales,'total':total,'change':change,'net':net})
def doll(request):
    dolls=Doll.objects.all()
    return render(request,'doll.html',{'dolls':dolls})

def arrival(request):
    arrivals=Arrival.objects.all()
    return render(request,'arrival.html',{'arrivals':arrivals})
  
def addsarrival(request):
      if request.method=='POST':
        form=ArrivalForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('arrival')
      else:
        form=ArrivalForm()
      return render(request,'addsarrival.html',{'form':form })         
  
def readsarrival(request, baby_id):  # Add id parameter to the view function
    arrival_info = Arrival.objects.get(id=baby_id)  # Retrieve Departure object using the provided id
    return render(request, 'readsarrival.html', {'arrival_info': arrival_info})  # Render 'readdeparture.html' template with departure_info

def editsarrival(request,id):
     arrivals=get_object_or_404(Arrival,id=id)
     if request.method == 'POST':  
       form=ArrivalForm(request.POST,instance=arrival)
       if form.is_valid():
           form.save()
           return redirect('arrival')
     else:
            form=ArrivalForm(instance=arrivals) 
     return render(request,'editsarrival.html',{'form':form,'arrivals':arrivals})     

def departure(request):
  departure=Departure.objects.all()
  return render(request,'departure.html',{'departure':departure})


def adddeparture(request):
   if request.method=='POST':
        form=DepartureForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('departure')
   else:
            form=DepartureForm()
   return render(request,'addsarrival.html',{'form':form })      
  

def readdeparture(request, id):  # Add id parameter to the view function
    departure_info = Departure.objects.get(id=id)  # Retrieve Departure object using the provided id
    return render(request, 'readdeparture.html', {'departure_info': departure_info})  # Render 'readdeparture.html' template with departure_info

def editdeparture(request):
     departures=get_object_or_404(Departure,id=id)
     if request.method == 'POST':  
       form=DepartureForm(request.POST,instance=arrival)
       if form.is_valid():
           form.save()
           return redirect('departure')
     else:
            form=DepartureForm(instance=departures) 
     return render(request,'editsarrval.html',{'form':form,'departures':departure})     



def onduty(request):
  onduty=Sitter_arrival.objects.all()
  return render(request,'onduty.html',{'onduty':onduty})
  return render(request,'onduty.html')

def addonduty(request):
   if request.method=='POST':
        form=Sitter_arrivalForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('onduty')
   else:
            form=DepartureForm()
   return render(request,'addsonduty.html',{'form':form })      
  

def readonduty(request):
   baby_info=Payment.objects.get(id=id)
   return render(request,'readonduty.html')

def editonduty(request):
    departures=get_object_or_404(Departure,id=id)
    if request.method == 'POST':  
       form=DepartureForm(request.POST,instance=arrival)
       if form.is_valid():
           form.save()
           return redirect('onduty')
    else:
            form=DepartureForm(instance=departures) 
    return render(request,'editsarrval.html',{'form':form,'departures':departure})     











 