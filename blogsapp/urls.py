from django.urls import path
from blogsapp import views

urlpatterns = [path('blogs/',views.blogs,name='blogs'),]
