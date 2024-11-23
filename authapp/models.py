from django.db import models
# extending user model to set our own user table
from django.contrib.auth.models import AbstractUser

# User table
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN",'Admin'
        STUDENT = "STUDENT",'Student'
        VISITOR = " VISITOR ",'Visitor'
    
    # Admin data
    base_role = Role.ADMIN
    
    # new field
    role = models.CharField(max_length=50,choices=Role.choices)
    
    # assign default role during signup
    def save(self,*args,**kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args,**kwargs) 