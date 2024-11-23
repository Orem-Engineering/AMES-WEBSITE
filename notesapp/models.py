from django.db import models
from PIL import Image

# Create your models here.
# Notes models here.
class Notes(models.Model):
  unit_name = models.CharField(max_length=10)
  category = models.CharField(max_length=100,default='')
  subcategory = models.CharField(max_length=100,default='')
  year_issued = models.CharField(max_length=10,default="first year,second year,third year,fourth year,fifth year")
  engineering_group = models.CharField(max_length=10,default="B Eng,B Tech,Diploma,Artisan")
  notes_content= models.FileField(upload_to='notes',max_length=None,null=True,blank=True)
  upload_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
  def __str__(self):
        return self.unit_name
