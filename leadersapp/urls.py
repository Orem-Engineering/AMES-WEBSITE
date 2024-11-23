from django.urls import path
from leadersapp import views

urlpatterns = [
    path('executive/',views.executive,name='executive'),
    path('about',views.about,name='about')
    ]