from django.db import models
from PIL import Image

# Create your models here.

# Pastpaper models here.
class Pastpaper(models.Model):
  unit_name = models.CharField(max_length=10)
  category = models.CharField(max_length=100,default='semester one')
  subcategory = models.CharField(max_length=100,default='')
  year_done= models.CharField(max_length=10,default="first year,second year,third year,fourth year,fifth year")
  lecturer_who_set_the_paper = models.CharField(max_length=100,default='')
  engineering_group = models.CharField(max_length=10,default="B Eng,B Tech,Diploma,Artisan")
  paper_upload= models.FileField(upload_to='PastPapers',max_length=None,null=True,blank=True)
  upload_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
  def __str__(self):
        return self.unit_name
  
  