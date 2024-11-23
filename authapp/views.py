
# Create your views here.
from django.shortcuts import render,redirect
# getting default user models
from django.contrib.auth.models import User 
#authentication library
from django.contrib.auth import authenticate,login,logout
# messages library
from django.contrib import messages
# login decorator library
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
#Signup function
def signup(request):
    # getting ing user inputs
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('password1') 
        get_cornfirm_password = request.POST.get('password2')
        # checking if two password match
        if  get_password != get_cornfirm_password:
            messages.info(request,"Passwords doesn't match")
            return redirect('/auth/signup/')
        # checking if email exists
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"Email is taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        # creating the new user
        # passing get_email as both username and email and get_password as the password
        myuser = User.objects.create_user(get_email,get_email,get_password)
        myuser.save()
        messages.success(request,'User created successfully.Please login.')
        # redirecting to login page
        return redirect('/auth/login/')
    
    return render(request,'signup.html')

def handlelogin(request):
    # getting ing user inputs
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('password1')
        # authenticating the user using username and password
        myuser = authenticate(username=get_email,password=get_password) 
        
        # loging in the user
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,'login.html')

# logout function
@ login_required(login_url='signin/')
def handlelogout(request):
    logout(request)
    messages.success(request,'Logout success')
    return render(request,'login.html')

