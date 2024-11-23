from django.db import models
from PIL import Image

# Create your models here.
# OFFICIALS MODEL
# patrons model 
class Patron(models.Model):
  Patrons_Name = models.CharField(max_length=50)
  Status = models.CharField("current or former",max_length=15)
  Patrons_Photo = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,default='blank-profile-picture.png')
  #photoDate = models.DateTimeField(auto_now=True)
  Patrons_Attributes = models.CharField(help_text="Attributes abouts the club",max_length=15,default="Patrons attributes")
  
  def __str__(self):
    return (self.Patrons_Name)
  
    
# chairperson model
class Chairperson(models.Model):
  chairperson_name = models.CharField(max_length=100)
  status = models.CharField("current or former",max_length=15)
  chairperson_photo = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,null=True,default='blank-profile-picture.png')
  #photoDate = models.DateTimeField(auto_now=True)
  chairperson_attributes = models.CharField(help_text="Attributes abouts the club",max_length=15)
 
  #photoDate = models.DateTimeField(auto_now=True)
  def __str__(self):
    return (self. chairperson_name)

    
# tresurer model
class Tresurer(models.Model):
  tresurer_name = models.CharField(max_length=70)
  status = models.CharField("current or former",max_length=15)
  officialPhoto = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,default='blank-profile-picture.png')
  tresurer_attributes = models.CharField(help_text="Attributes abouts the club",max_length=15)
  photoDate = models.DateTimeField(auto_now=True)
  def __str__(self):
    return (self. tresurer_name)
 
  # secretary  model
class Secretary(models.Model):
  secretary_name = models.CharField(max_length=50)
  status = models.CharField("current or former",max_length=15)
  secretary_photo = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,default='blank-profile-picture.png')
  #photoDate = models.DateTimeField(auto_now=True)
  secretary_attributes = models.CharField(help_text="Attributes abouts the club",max_length=15)
  def __str__(self):
    return self.secretary_name

    
# media model 
class Mediateam(models.Model):
  mediateam_name = models.CharField(max_length=70)
  status = models.CharField("current or former",max_length=15)
  officialPhoto = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,default='blank-profile-picture.png')
  photoDate = models.DateTimeField(auto_now=True)
  mediateam_attributes = models.CharField(help_text="Attributes abouts the club",max_length=15)
  def __str__(self):
    return (self.mediateam_name,self.position)
 
    
# assistant chairperson model
class AssistantChairperson(models.Model):
  assistantChairperson_name = models.CharField(max_length=70)
  status = models.CharField("current or former",max_length=15)
  assistantChairperson_photo = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,null=True,default='blank-profile-picture.png')
  #photoDate = models.DateTimeField(auto_now=True)
  assistantChairperson_attributes = models.CharField(help_text="Attributes abouts the club",max_length=15)
  def __str__(self):
    return (self.assistantChairperson_name)
    
  #Assiatant tresurer model
class AssiatantTresurer(models.Model):
  assiatantTresurer_name = models.CharField(max_length=70)
  status = models.CharField("current or former",max_length=15)
  assiatantTresurer_photo = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,null=True,default='blank-profile-picture.png')
  #photoDate = models.DateTimeField(auto_now=True)
  assiatantTresurer_attributes = models.CharField(help_text="Attributes abouts the club",max_length=15)
  def __str__(self):
    return (self.assiatantTresurer_name)

    
  # Assiatant secretary  model
class AssiatantSecretary(models.Model):
  assiatantSecretary_name = models.CharField(max_length=70)
  status = models.CharField("current or former",max_length=15)
  assiatantSecretary_photo = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,null=True,default='blank-profile-picture.png')
  #photoDate = models.DateTimeField(auto_now=True)
  assiatantSecretary_attributes = models.CharField(help_text="Attributes abouts the club",max_length=15)
  def __str__(self):
    return (self.assiatantSecretary_name)
  
    
# Organising secretary  model
class OrganisingSecretary(models.Model):
  organisingSecretary_name = models.CharField(max_length=70)
  status = models.CharField("current or former",max_length=15)
  organisingSecretary_photo = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,null=True,default='blank-profile-picture.png')
  #photoDate = models.DateTimeField(auto_now=True)
  organisingSecretary_attributes = models.CharField(help_text="Attributes abouts the club",max_length=15)
  def __str__(self):
    return (self.organisingSecretary_name)

    
# Testimonial model 
class Testimonial(models.Model):
  Testimonial_Name = models.CharField(max_length=70,help_text="Name of Testimonial ")
  Testimonial_Position = models.CharField(help_text="Role in the club",max_length=30)
  Testimonial_Photo = models.ImageField(upload_to='profile_image/',height_field=None,width_field=None,max_length=None,null=True,default='blank-profile-picture.png',help_text="Picure of Testimonial person")
  Testimonial_Attributes = models.CharField(max_length=25,help_text="Positive attributes only of maximum length of 25 words")
  # Renaming verbose 
  class Meta:
      verbose_name = "Testimonial"
      verbose_name_plural = "Testimonials"
  
  def __str__(self):
    return (self.Testimonial_Name,self.Testimonial_Position)


