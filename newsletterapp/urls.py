from django.urls import path
from newsletterapp import views

urlpatterns = [
    path('subscription/',views.subscription,name='subscription'),
    ]