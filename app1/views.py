from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')

#home page loader
def homepage(request):
    return render(request,'home.html')

#login page loader
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password doesnt match')
        
    return render(request,'login.html')

#signup page loader
def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse('passwords do not match!!')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        
        return redirect('login')
        
    return render(request,'signup.html')

#logout button loader
def logoutpage(request):
    logout(request)
    return redirect('login')