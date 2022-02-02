from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name="accounts"

urlpatterns = [
     url('/login/', views.login_view, name='login'),
     url('/logout/',views.logout_view, name='logout'),
]
