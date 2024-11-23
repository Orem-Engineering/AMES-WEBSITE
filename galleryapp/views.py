from django.shortcuts import render
from galleryapp.models import Picture

# Create your views here.
# gallery views .
def gallery(request):
  pictures = Picture.objects.all()
  return render(request,'gallery.html',{'pictures':pictures} )


  