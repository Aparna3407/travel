from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        name=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Login")
            return redirect('login')

    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        name=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=name).exists():
                messages.info(request,"Username Taken")
                return redirect("register")
            if User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect("register")
            else:
                user=User.objects.create_user(username=name,email=email,password=password)
                user.save();
                print("user created")
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('/register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
