from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',auth_views.LoginView.as_view(template_name ='login.html'), name = 'login'),
    path('home/', views.home, name='home'),
    path('logout/',views.log_out, name = 'logout'),
    path('babiesform/', views.babiesform, name='babiesform'),
    path('add/', views.add, name='add'),
    path('read/<int:id>/', views.read, name='read'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('sitterform/', views.sitterform, name='sitterform'),
    path('adds/', views.adds, name='adds'),
    path('reads/<int:id>/', views.reads, name='reads'),
    path('edits/<int:id>/', views.edits, name='edits'),

   
    #dollscorner
    path('doll/',views.doll,name='doll'),
    path('dolladd/',views.dolladd,name='dolladd'),
    path('dollscorner/<int:doll_id>/', views.dollscorner, name='dollscorner'),
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),
    path('all_sales/',views.all_sales,name='all_sales'),
    path('issue_item/<str:pk>',views.issue_item,name='issue_item'),
    path('receipt/',views.receipt,name='receipt'),
    path('receipt_detail/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),
    path('dolledit/<int:id>/',views.dolledit,name='dolledit'),

    path('departure/', views.departure, name='departure'),
    path('adddeparture/', views.adddeparture, name='adddeparture'),
    path('readdeparture/<int:baby_id>/', views.readdeparture, name='readdeparture'),
    path('editdeparture/<int:id>/', views.editdeparture, name='editdeparture'),
    #sitteronduty
    path('onduty/', views.onduty, name='onduty'),
    path('addonduty/', views.addonduty, name='addonduty'),
    path('readonduty/<int:id>/', views.readonduty, name='readonduty'),
    path('editdontudy/<int:id>/', views.editonduty, name='editonduty'),
    
    
    #procurement
    path('inventories/', views.inventories, name='inventories'),
    path('add_to_stocks/<str:pk>', views.add_to_stocks, name='add_to_stocks'),
    path('all_issue_items/',views.all_issue_items,name='all_issue_items'),
    path('issue/<str:pk>',views.issue,name='issue'),
    path('inventoryform/', views.inventoryform, name='inventoryform'),
    path('inventoryedit/<int:id>/', views.inventoryedit, name='inventoryedit'),
    
#sitterpayment
    path('create_payment/', views.create_payment, name='create_payment'),
    path('payment_list/', views.payment_list, name='payment_list'),
    path('edit_paymentsitter/<int:id>/', views.edit_paymentsitter, name='edit_paymentsitter'),

   

#payment for babies    
 path('paymentform/', views.paymentform, name='paymentform'),
 path('payment_lists/', views.payment_lists, name='payment_lists'),
 path('edit_payment/<int:id>/', views.edit_payment, name='edit_payment'),


 #sitterdeparture
 path('sitterdeparture/', views.sitterdeparture, name='sitterdeparture'),
 path('addsitter/', views.addsitter, name='addsitter'),
 path('reasitter/<int:id>/', views.readsitter, name='readsitter'),
 path('editsitter/<int:id>/', views.editsitter, name='editsitter'),
    
]
    

