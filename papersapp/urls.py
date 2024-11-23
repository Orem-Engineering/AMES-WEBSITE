from papersapp import views
from django.urls import path

urlpatterns = [
    path('pastpapers/', views.pastpapers,name='pastpapers'),
    ]