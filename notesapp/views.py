from django.shortcuts import render,redirect
from notesapp.models import Notes
# login decorator library
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
# math library for categoring notes
from math import ceil

# Create your views here.
#notes content view, recheck the html file
@ login_required(login_url='signin/')
def note(request):
    #categorising notes using category and id
    all_notes = []
    categorised_notes = Notes.objects.values('category','id')
    # passing the notes to a list
    categories = {item['category'] for item in categorised_notes}
    #filtering all categories
    for categgory in categories:
        notes = Notes.objects.filter(category=categgory)
        # displaying four notes in a row using a formula
        n = len(notes)
        # formulae
        nSlides = n//4 + ceil((n/4)-(n//4))
        all_notes.append([notes,range(1,nSlides),nSlides])
    context = {'all_notes':all_notes}
    return render (request,'notes.html',context)
  
