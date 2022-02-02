from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name="Timetable"

urlpatterns = [
     url('/timetable/', views.timetable, name='Timetable'),
     url('/feedback/',views.feedback, name='Feedback'),
     url('/view_Grades/', views.view_Grades, name='View Grades'),
]