from notesapp import views
from django.urls import path

urlpatterns = [
    path('notes/', views.note,name='notes'),
    ]