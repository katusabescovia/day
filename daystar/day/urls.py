from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',auth_views.LoginView.as_view(template_name ='login.html'), name = 'login'),
    path('home/', views.home, name='home'),
    path('logout/',auth_views.LogoutView.as_view(template_name ='logout.html'), name = 'logout'),
    path('babiesform/', views.babiesform, name='babiesform'),
    path('add/', views.add, name='add'),
    path('read/<int:id>/', views.read, name='read'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('sitterform/', views.sitterform, name='sitterform'),
    path('adds/', views.adds, name='adds'),
    path('reads/<int:id>/', views.reads, name='reads'),
    path('edits/<int:id>/', views.edits, name='edits'),
    path('paymentform/', views.paymentform, name='paymentform'),
    path('addpay/', views.addpay, name='addpay'),
    path('readpay/<int:id>/', views.readpay, name='readpay'),
    path('editpay/<int:id>/', views.editpay, name='editpay'),
    

    

]