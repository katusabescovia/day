from django.shortcuts import render,redirect,get_object_or_404
from django .contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from .forms import *
from . models import *
# from .forms import BabiesformForm
# from .models import Babiesfor


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')

def logout(request):
    return render(request,'logout.html')
def sitterpayment(request):
    return render(request,'sitterpayment.html')

def babiesform(request):
    babies= Babiesform.objects.all()
    return render(request,'babiesform.html',{'babies':babies})
    

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
    
        

def read(request,id):
   babies_info=Babiesform.objects.get(id=id)
   return render(request,'read.html',{'babies_info':babies_info})


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
        
    


def sitterform(request):
    sitters=Sitterform.objects.all()
    return render(request,'sitterform.html',{'sitters':sitters})
    



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

    

def reads(request,id):
    sitters_info=Sitterform.objects.get(id=id)
    return render(request,'reads.html',{'sitters_info':sitters_info})
    




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
        

    

 
