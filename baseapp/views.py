
from django.shortcuts import render,redirect,HttpResponse
# login decorator library
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
#importig user models and authentication
from django.contrib.auth.models import User,auth
# message library
from django.contrib import messages

# importing database models 
from baseapp.models import Constitution
from baseapp.models import Inqury
from leadersapp.models import Chairperson
from leadersapp.models import Patron
from baseapp.models import ThirdHomepagePicture
from baseapp.models import FirstHomepagePicture
from baseapp.models import SecondHomepagePicture
from leadersapp.models import *


# Create your views here.
#home function.
def homepage(request):
  # patron
  patron = Patron.objects.all()
  context2 = {'patron':patron}
  # chairperson
  chairperson = Chairperson.objects.all()
  context3 = {'chairperson':chairperson}
  #first  homepage image
  firstimg = FirstHomepagePicture.objects.all()
  context4 = {'firstimg':firstimg}
  # second  homepage image
  secondimg = SecondHomepagePicture.objects.all()
  context5 = {'secondimg ':secondimg }
  # third  homepage image
  thirdimg = ThirdHomepagePicture.objects.all()
  context6 = {'thirdimg':thirdimg}
  #dispalying all
  finalcontext = [context2,context3,context4 ,context5  ,context6]
  return render(request,'index.html')

#constituton view
def constitution(request):
  constitution = Constitution.objects.all()
  context = {'constituition':constitution}
  return render (request,'constitution.html',context)

#contactsus view
def contacts(request):
  if request.method == "POST":
    contactname = request.POST['contactname']
    contactemail = request.POST['contactemail']
    contactsubject = request.POST['contactsubject']
    contactmessage = request.POST['contactmessage']
    
    # saving the contact message
    inquiry = Inqury(contactname=contactname,contactmessage=contactmessage,contactemail=contactemail,contactsubject=contactsubject)
    inquiry.save()
    messages.success(request,'Your message has been sent. Thank you!')
  return render(request,'contact.html')

# membership view
def membership(request):
  return render(request,'membership.html')


