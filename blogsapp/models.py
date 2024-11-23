from django.db import models
from PIL import Image

# Create your models here.
#Notice table
class Blogs(models.Model):
  Notice_Heading = models.CharField(help_text="Notice Heading",max_length=60,default="Notice One")
  Notice_Content = models.TextField()
  Notice_of_Date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
  Notice_Poster = models.ImageField(upload_to='notices')
  Notice_Uploaded_By = models.CharField(max_length=20,default='Media team')
  
  def __str__(self):
    return  self.Notice_Heading