from django.shortcuts import render,redirect,get_object_or_404
from django .contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .models import *
from django.contrib.postgres.search import SearchQuery, SearchVector
from . filters import *
from django.http import HttpResponseBadRequest
from django.db.models import Sum

# from .forms import BabiesformForm
# from .models import Babiesfor


# Create your views here.

def index(request):
    return render(request,'index.html')
@login_required
def log_out(request):
    logout(request)
    return redirect('/')

@login_required
def home(request):
    return render(request,'home.html')


@login_required
def sitterpayment(request):
    return render(request,'sitterpayment.html')
#Babies registrations
@login_required
def babiesform(request):
    babies= Babiesform.objects.all().order_by('id')
    baby_filters=Baby_Filter(request.GET,queryset=babies)
    babies=baby_filters.qs
    return render(request,'babiesform.html',{'babies':babies, 'baby_filters':baby_filters})
 
    
    
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
        
    
#sittersregistrations
@login_required
def sitterform(request):
    sitters=Sitterform.objects.all().order_by('id')
    sitter_filters=SitterFilter(request.GET,queryset=sitters)
    sitters=sitter_filters.qs
    return render(request,'sitterform.html',{'sitters':sitters,'sitter_filters':sitter_filters})
    
    


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



 #dollscorner
@login_required
def dollscorner(request, doll_id):
    doll = get_object_or_404(Doll, id=doll_id)
    return render(request, 'dollscorner.html', {'doll': doll})


@login_required
def receipt(request):
    sales= Salesrecord.objects.all().order_by('id') 
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
def add_to_stock(request, pk):
    issued_item = Doll.objects.get(id=pk)
    if request.method == 'POST':
        form = Addform(request.POST)
        if form.is_valid():
            received_quantity = request.POST.get('received_quantity')
            if received_quantity:
                try:
                    added_quantity = int(received_quantity)
                    issued_item.quantity += added_quantity
                    issued_item.save()
                    print(added_quantity)
                    print(issued_item.quantity)
                    return redirect('doll')
                except ValueError:
                    return HttpResponseBadRequest("Invalid quantity")
    else:
        form = Addform()
    return render(request, 'add_to_stock.html', {'form': form})



@login_required
def all_sales(request):
    sales=Salesrecord.objects.all()
    total=sum([items.amount_received for items in sales])
    change=sum([items.get_change() for items in sales])
    net=total-change
    return render(request,'all_sales.html',{'sales':sales,'total':total,'change':change,'net':net})
@login_required
def doll(request):
    dolls=Doll.objects.all().order_by('id')
    doll_filters=DollFilter(request.GET,queryset=dolls)
    dolls=doll_filters.qs
    return render(request,'doll.html',{'dolls':dolls,'doll_filters':doll_filters})
   

@login_required
def dolladd(request):
    if request.method=='POST':
        form=Address_form(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('doll')
    else:
        form=Address_form()
    return render(request,'dolladd.html',{'form':form})

def dolledit(request,id):
    doll=get_object_or_404(Doll,id=id)
    if request.method == 'POST':
       form=Address_form (request.POST,instance=doll)
       if form.is_valid():
           form.save()
           return redirect('doll')
    else:
        form=Address_form(instance=doll)
    return render(request,'dolledit.html',{'form':form,'doll':doll})     


#babies departure
@login_required
def departure(request):
  babys=Departure.objects.all().order_by('id')
  baby_filters=Departure_Filter(request.GET,queryset=babys)
  babys=baby_filters.qs
  return render(request,'departure.html',{'babys':babys,'baby_filters':baby_filters})



@login_required
def adddeparture(request):
   if request.method=='POST':
        form=DepartureForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('departure')
   else:
            form=DepartureForm()
   return render(request,'adddeparture.html',{'form':form })      
  
@login_required
def readdeparture(request, baby_id):  # Add id parameter to the view function
    departure_info = Departure.objects.get(id=baby_id)  # Retrieve Departure object using the provided id
    return render(request, 'readdeparture.html', {'departure_info': departure_info})  # Render 'readdeparture.html' template with departure_info

def editdeparture(request,id):
     departures=get_object_or_404(Departure,id=id)
     if request.method == 'POST':  
       form=DepartureForm(request.POST,instance=departures) 
       if form.is_valid():
           form.save()
           return redirect('departure')
     else:
            form=DepartureForm(instance=departures) 
     return render(request,'editdeparture.html',{'form':form,'departures':departures})     


#sitter onduty
@login_required
def onduty(request):
  onduty=Sitter_arrival.objects.all().order_by('id')
  onduty_filters=Sitter_arrivalFilter(request.GET,queryset=onduty)
  onduty=onduty_filters.qs
  return render(request,'onduty.html',{'onduty':onduty,'onduty_filters':onduty_filters})
  

    
def addonduty(request):
   if request.method=='POST':
        form=Sitter_arrivalForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('onduty')
   else:
            form=Sitter_arrivalForm()
   return render(request,'addonduty.html',{'form':form })      
  

def readonduty(request ,id):
   sitter_info=Sitter_arrival.objects.get(id=id)
   return render(request,'readonduty.html',{'sitter_info':sitter_info})

def editonduty(request, id):
    onduty=get_object_or_404(Sitter_arrival,id=id)
    if request.method == 'POST':  
       form=Sitter_arrivalForm(request.POST,instance=onduty)
       if form.is_valid():
           form.save()
           return redirect('onduty')
    else:
            form=Sitter_arrivalForm(instance=onduty) 
    return render(request,'editonduty.html',{'form':form,'onduty':onduty})     
#inventories
@login_required
def add_to_stocks(request, pk):
    issued_procurement = Procurement.objects.get(id=pk)
    
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            received_quantity = form.cleaned_data.get('received_quantity')
            added_quantity = int(received_quantity)
            issued_procurement.Quantity += added_quantity

            issued_procurement.save()
            return redirect('inventories')  
    else:
        form = AddForm()
    
    return render(request, 'add_to_stocks.html', {'form': form})

@login_required
def inventories(request):
    inventory=Procurement.objects.all().order_by('id')
    product_filters=ProcurementFilter(request.GET,queryset=inventory)
    inventory=product_filters.qs
    return render(request,'inventories.html',{'inventory':inventory,'product_filters':product_filters})
   
def issue(request, pk):
    issued_item = Procurement.objects.get(id=pk) 
    issue_form = Usedlogform(request.POST)  

    if request.method == 'POST':
        if issue_form.is_valid():
            new_issue = issue_form.save(commit=False)
            new_issue.item = issued_item
            new_issue.save()
            issued_quantity = int(request.POST['quantity_issued'])
            issued_item.Quantity -= issued_quantity

            issued_item.save()
            print(issued_item.item_name)
            print(request.POST['quantity_issued'])
            print(issued_item.Quantity)
            return redirect('inventories')
    return render(request, 'issue.html', {'issue_form': issue_form})

def all_issue_items(request):
    issued_items=Usedlog.objects.all()
    return render(request,'all_issue_items.html',{'issued_items':issued_items})
@login_required
def all_issue_items(request):
    issues = Usedlog.objects.all()
    total_issued_quantity = issues.aggregate(total_issued_quantity=Sum('quantity_issued'))['total_issued_quantity'] or 0
    
    # Calculating total received quantity
    total_received_quantity = Procurement.objects.aggregate(total_received_quantity=Sum('Quantity'))['total_received_quantity'] or 0
    
    # Calculating net quantity
    net_quantity = total_received_quantity - total_issued_quantity

    return render(request, 'all_issue_items.html', {'issues': issues, 'total_issued_quantity': total_issued_quantity, 'total_received_quantity': total_received_quantity, 'net_quantity': net_quantity})

def inventoryform(request):
    if request.method == 'POST':
        form = Add_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventories')
    else:
        form = Add_form()
    return render(request, 'inventoryform.html', {'form': form})
def inventoryedit(request,id):
    inventory=get_object_or_404(Procurement,pk=id)
    if request.method == 'POST':
       form=Add_form (request.POST,instance=inventory)
       if form.is_valid():
           form.save()
           return redirect('inventories')
    else:
        form=Add_form(instance=inventory)
    return render(request,'inventoryedit.html',{'form':form,'inventory':inventory})     
 

#sitterpayment
def create_payment(request):
    if request.method == 'POST':
        form = SitterpaymentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the payment list page upon successful form submission
            return redirect('payment_list')
    else:
        form = SitterpaymentForm()
    

    return render(request, 'create_payment.html', {'form': form})


def payment_list(request):
  payments=Sitterpayment.objects.all().order_by('id')
  payment_filter=SitterpaymentFilter(request.GET,queryset=payments)
  payments=payment_filter.qs
  return render(request,'payment_list.html',{'payments':payments,'payment_filter':payment_filter})
 

def edit_paymentsitter(request,id):
    payment=get_object_or_404(Sitterpayment,id=id)
    if request.method == 'POST':  
       form=SitterpaymentForm(request.POST,instance=payment)
       if form.is_valid():
           form.save()
           return redirect('payment_list')
    else:
            form=SitterpaymentForm(instance=payment) 
    return render(request,'edit_paymentsitter.html',{'form':form,'payment':payment})

#payment for babies
def payment_lists(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the payment list page upon successful form submission
            return redirect('paymentform')
    else:
        form = PaymentForm()
    

    return render(request, 'payment_lists.html', {'form': form})


def paymentform(request):
  payment_list=Payment.objects.all().order_by('id')
  payment_filter=payment_Filter(request.GET,queryset=payment_list)
  payment_list=payment_filter.qs
  return render(request,'paymentform.html',{'payment_list':payment_list, 'payment_filter':payment_filter})


 

def edit_payment(request,id):
    payment=get_object_or_404(Payment,id=id)
    if request.method == 'POST':  
       form=PaymentForm(request.POST,instance=payment)
       if form.is_valid():
           form.save()
           return redirect('paymentform')
    else:
            form=PaymentForm(instance=payment) 
    return render(request,'edit_payment.html',{'form':form,'payment':payment})


#views for Sitters departure
def sitterdeparture(request):
    sitters=Sitter_departure.objects.all().order_by('id')
    sitter_filters=Sitter_departureFilter(request.GET,queryset=sitters)
    sitters=sitter_filters.qs
    return render(request,'sitterdeparture.html',{'sitters':sitters,'sitter_filters':sitter_filters})


    
def addsitter(request):
    if request.method == 'POST':
        form=Sitter_departureform(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('sitterdeparture')
    else:
        form=Sitter_departureform()    
    return render(request,'addsitter.html',{'form': form})

 
def readsitter(request,id):
    sitter_info=Sitter_departure.objects.get(id=id)
    return render(request,'readsitter.html',{'sitter_info':sitter_info})

def editsitter(request,id):
    sitter=get_object_or_404(Sitter_departure,id=id)
    if request.method == 'POST':  
       form=Sitter_departureform(request.POST,instance=sitter)
       if form.is_valid():
           form.save()
           return redirect('sitterdeparture')
    else:
            form=Sitter_departureform(instance=sitter) 
    return render(request,'editsitter.html',{'form':form,'sitter':sitter})     

#dashboard

def dashboard(request):
    count_babies = Babiesform.objects.count()
    count_sitters = Sitterform.objects.count()
    babypayment=Payment.objects.aggregate(Sum('amount_paid'))
    total_amount_paid = babypayment.get('amount_paid__sum', 0)
    babypaymentfordoll=Salesrecord.objects.aggregate(Sum('amount_received'))
    total_amount_received = babypaymentfordoll.get('amount_received__sum', 0)
    totalpayments=total_amount_received+total_amount_paid
    recent_babies = Babiesform.objects.all()[:3]  # Getting the two most recent Babyreg objects
    recent_sitters = Sitterform.objects.all()[:3]  # Getting the two most recent 
    context = {'count_babies': count_babies, 'count_sitters':count_sitters,
               
        'totalpayments': totalpayments,'recent_sitters': recent_sitters,'recent_babies': recent_babies}
    
    return render(request, 'dashboard.html', context)


 