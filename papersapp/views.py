from django.shortcuts import render,redirect
from papersapp.models import Pastpaper
# login decorator library
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
# math library for categoring notes
from math import ceil

# Create your views here.

#past paper content view, recheck the html file
@ login_required(login_url='signin/')
def pastpapers(request):
    #categorising notes using category and id
    all_papers = []
    categorised_papers = Pastpaper.objects.values('category','id')
    # passing the notes to a list
    categories = {item['category'] for item in categorised_papers}
    #filtering all categories
    for categgory in categories:
        papers = Pastpaper.objects.filter(category=categgory)
        # displaying four notes in a row using a formula
        n = len(papers)
        # formulae
        nSlides = n//4 + ceil((n/4)-(n//4))
        all_papers.append([papers,range(1,nSlides),nSlides])
    context = {'all_notes':all_papers}
    return render (request,'papers.html',context)
              