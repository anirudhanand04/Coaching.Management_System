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