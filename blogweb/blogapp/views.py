from django.shortcuts import render
from django.http import request,HttpResponseRedirect
from django.contrib.auth  import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,'index.html')

#REGISTRATION FORM
def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email= request.POST['email']
        password= request.POST['pass']
        confpass= request.POST['cpass']
        if password == confpass:
            pass
        else:
            msg="password and confirmpassword doesn't mached"
    else:
        # return HttpResponseRedirect('reg')
        return render(request,'auth/register.html',{'msg': msg})

#login form
@login_required()
def login(request):
    return render(request,'auth/login.html')
