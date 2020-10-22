from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import *
from .forms import *

def home(request):
    allBusinesses = Business.objects.all() 

    context = {
        "businesses": allBusinesses, 
    }
    
    return render(request,'main/index.html', context)
    
    
#details page
def detail(request, id):
    business = Business.objects.get(id=id) 

    context = {
        "business": business
    }
    return render(request, 'main/details.html', context)


def add_business(request):
        if request.method == "POST":
            form = BusinessForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect("main:home")
        else:
            form = BusinessForm()
        return render(request, 'main/addbusiness.html', {"form": form, "controller": "Add a business"})

def edit_business(request, id):
    
    busines = Business.objects.get(id=id)
    
    if request.method == "POST":
        form = BusinessForm(request.POST or None, instance=busines)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:detail", id)
    else:
        form = BusinessForm(instance=busines)
    return render(request, 'main/addbusiness.html', {"form": form, "controller": "Edit Business"})

def delete_business(request, id):
    business = Business.objects.get(id=id)
    business.delete()
    return redirect('main:home')