from django.db import models
from django.utils import timezone
from datetime import datetime 
from PIL import Image
# library for model of currently loged in user
from django.contrib.auth import get_user_model
#model of currently loged in user

# homepage galery image 1
class FirstHomepagePicture(models.Model):
  photo = models.ImageField(upload_to='homepage_photos/',default='blank-profile-picture.png')
  caption = models.CharField(max_length=200)
  
  #photoDate = models.DateTimeField(auto_now=True)

# homepage galery image 1
class SecondHomepagePicture(models.Model):
  photo = models.ImageField(upload_to='homepage_photos/',default='blank-profile-picture.png')
  caption = models.CharField(max_length=200)
 
  #photoDate = models.DateTimeField(auto_now=True)

 # homepage galery image 3
class ThirdHomepagePicture(models.Model):
  photo = models.ImageField(upload_to='homepage_photos/',height_field=None,width_field=None,max_length=None,null=True,blank=True,default='blank-profile-picture.png')
  caption = models.CharField(max_length=200)
  #photoDate = models.DateTimeField(auto_now=True)


# Inqury models .
class Inqury(models.Model):
  contactname = models.CharField(max_length=50,default="contact name")
  contactemail = models.CharField(max_length=70)
  contactsubject = models.EmailField(max_length=250)
  contactmessage = models.TextField(default=" contact message")
  
 
# Constitution models 
class Constitution(models.Model):
  
  Chapter = models.CharField("add chapter",max_length=250,null=True,blank=True)
  Added_article = models.TextField("add content of the article",null=True,blank=True)
  #updated_on =models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.Added_article
  
