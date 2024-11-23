from galleryapp import views
from django.urls import path
urlpatterns = [
    path('gallery/', views.gallery,name='gallery')]