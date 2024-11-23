from django.db import models
# from ckeditor.fields import RichTextField

# Create your models here.
# subsscriber model 
class Subscriber(models.Model):
    email = models.EmailField(unique=True,help_text="Newsletter subscribers email")
    
    class Meta:
        verbose_name = "Subscribers"
        
    def __str__(self):
        return self.email
    
# subsscriber model 
class EmailTemplate(models.Model):
    Subject = models.CharField(unique=True,help_text="email subject ",max_length=255)
   # Message = models.RichTextFields(unique=True,help_text="email subject ")
    Recipients = models.ManyToManyField(Subscriber,help_text="email subject ")
    
    
    class Meta:
        verbose_name = "Email Template"
        
    def __str__(self):
        return self.Subject 