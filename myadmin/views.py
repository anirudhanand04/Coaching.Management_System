from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import Courses

# Create your views here.
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            #log user in
            if user:
                login(request, user)
                #depending on user-type - redirect
                if request.POST['usertype']=='teacher':
                    return render(request, 'accounts/teacher.html')
                elif request.POST['usertype']=='admin':
                    return render(request, 'accounts/admin.html')
                elif request.POST['usertype']=='student' or  request.POST['usertype']=='User':
                    #get courses
                    courses = Courses.objects.all()
                    return render(request, 'accounts/student.html', {'courses': courses})
                else:
                    return HttpResponse(request.POST['usertype'] )
    else:
        form=AuthenticationForm(request)
    #Show the form, in case of login-error reshow the form
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')
    
def faculty_records(request):
    return render(request,'accounts\templates\accounts\new.html')
def ramankumar(request):
    return render(request, 'accounts\templates\accounts\raman.html')         
def anju_bala(request):
    return render(request, 'accounts\templates\accounts\anju.html')
def rakesh(request):
    return render(request, 'accounts\templates\accounts\ramesh.html')
def harkiran(request):
    return render(request, 'accounts\templates\accounts\Mrs Harkiran Kaur.html')
def vivek(request):
    return render(request, 'accounts\templates\accounts\Mr Vivek Bindra.html')
def ajay(request):
    return render(request, 'accounts\templates\accounts\Mr Ajay Kumar.html')
def geeta(request):
    return render(request, 'accounts\templates\accounts\Mrs Geeta Singh.html')
def sandeep(request):
    return render(request, 'accounts\templates\accounts\Mr Sandeep Sharma.html')
def ritu(request):
    return render(request, 'accounts\templates\accounts\Mrs Ritu Sharma.html')
# Create your views here.
