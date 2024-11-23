from django.shortcuts import render
from leadersapp.models import *

# Create your views here.
# excutive views 
def executive(request):
  # patron
  patron = Patron.objects.all()
  context2 = {'patron':patron}
  # chairperson
  chairperson = Chairperson.objects.all()
  context3 = {'chairperson':chairperson}
  # assistant chairperson
  assistant_chairperson = AssistantChairperson.objects.all()
  context4 = {'assistant_chairperson':assistant_chairperson}
  # assistant tresurer 
  assistant_tresurer  = AssiatantTresurer.objects.all()
  context5 = {'assistant_tresurer':assistant_tresurer}
  # Tresurer 
  tresurer  = Tresurer.objects.all()
  context6 = {'tresurer':tresurer}
  # Assistant Secretary
  assistant_secretary  = AssiatantSecretary.objects.all()
  context7 = {'assistant_secretary ':assistant_secretary }
  # Secretary
  secretary  = Secretary.objects.all()
  context8 = {'secretary ':secretary }
  # Mediateam
  mediateam  = Mediateam.objects.all()
  context9 = {'mediateam':mediateam }
  # Organising Secretary
  Organisingsecretary = OrganisingSecretary.objects.all()
  context2 = {'Organisingsecretary':Organisingsecretary }
  # dispaying all
  finalmembers = {'context2':context2,'context3':context3,'context4':context4,'context5':context5,'context6':context6,'context7':context7,'context8':context8,'context9':context9}

  return render (request,'executive.html',finalmembers)

# about function
def about(request):
  testimonial = Testimonial.objects.all()
  context = {'testimonial':testimonial}
  return render(request,'about.html',context)