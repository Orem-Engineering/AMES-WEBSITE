from authapp import views
from django.urls import path
urlpatterns = [
    path('signup/', views.signup,name='signup'),
    path('login/', views.handlelogin,name='handlelogin'),
    path('logout/', views.handlelogout,name='handlelogout'),
    ]