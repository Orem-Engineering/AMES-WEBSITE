
from django.urls import path
from baseapp import views

urlpatterns = [
  path('',views.homepage,name='homepage'),
  path('contact/',views.contacts,name='contacts'),
  path('membership/',views.membership,name='membership'),
  path('constitution/',views.constitution,name='constitution'),

]
