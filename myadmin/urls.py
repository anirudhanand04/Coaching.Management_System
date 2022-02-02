from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name="admin"

urlpatterns = [
     url('/login/', views.login_view, name='login'),
     url('/logout/',views.logout_view, name='logout'),
     url('/faculty_Records/',views.faculty_records, name='faculty_records'),
     path('/ramankumar',views.ramankumar,name='ramankumar'),
     path('/rakesh',views.rakesh,name='rakesh'),
     path('/anju_bala',views.anju_bala,name='Anju Bala'),
     path('/harkiran',views.harkiran,name='harkiran'),
     path('/vivek',views.vivek,name='Vivek Bindra'),
     path('/ajay',views.ajay,name='Ajay'),
     path('/geeta',views.geeta,name='Geeta'),
     path('/sandeep',views.sandeep,name='Sandeep'),
     path('/ritu',views.ritu,name='Ritu Sharma'),
]
