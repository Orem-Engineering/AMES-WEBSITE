from django.shortcuts import render
from blogsapp.models import *

# Create your views here.
# notifications views 
def blogs(request):
  notices = Blogs.objects.all()
  context = {'notices':notices  }
  return render (request,'events.html',context)
