from django.db import models
from PIL import Image

# Create your models here.
# Picture models here.
class Picture(models.Model):
  photo = models.ImageField(upload_to='fieldtrips_photos/',height_field=None,width_field=None,max_length=None,null=True,blank=True)
  picture_title = models.CharField(max_length=60)
  caption = models.CharField(max_length=200,default="picture caption")
  place = models.CharField("Place or location of the trip",max_length=400,null=True,blank=True)
  photoDate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
  def __str__(self):
    return self.picture_title