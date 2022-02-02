from django.shortcuts import render
from django.contrib.auth import timetable, feedback

def timetable(request):
    return render(request, 'templates\timetable.html')
def feedback(request):
    return render(request, 'templates\Feedback.html')
def view_Grades(request):
    return render(request, 'templates\view_Grades.html')

# Create your views here.
