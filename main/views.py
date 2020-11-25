from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import *
from .forms import *
from django.db.models import Avg

def home(request):
    query = request.GET.get("name")
    allBuinesses = None
    if query:
        allBusinesses = Business.objects.filter(name__icontains=query)
    else:

        allBusinesses = Business.objects.all() 

    context = {
        "businesses": allBusinesses, 
    }
    
    return render(request,'main/index.html', context)
    
    
#details page
def detail(request, id):
    business = Business.objects.get(id=id) 
    reviews = Review.objects.filter(business=id)
    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average, 2)
    context = {
        "business": business,
        "reviews":reviews,
        "average":average
    }
    return render(request, 'main/details.html', context)


def add_business(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BusinessForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect("main:home")
        else:
            form = BusinessForm()
        return render(request, 'main/addbusiness.html', {"form": form, "controller": "Add a business"})
    else:
        return redirect("main:home")


def edit_business(request, id):
    if request.user.is_authenticated:
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
    else:
          return redirect("main:home")


def delete_business(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            business = Business.objects.get(id=id)
            business.delete()
            return redirect('main:home')
        else:
            return redirect("main:home")
    return redirect("accounts:login")


def add_review(request, id):
    if request.user.is_authenticated:
        business = Business.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.business = business
                data.save()
                return redirect("main:detail", id)
        else:
            form = ReviewForm()
        return render(request, 'main/detail.html', {"form": form})
    else:
        return redirect("accounts:login")


def edit_review(request, business_id, review_id):
    if request.user.is_authenticated:
        business = Business.objects.get(id=business_id)
        review = Review.objects.get(business=business, id=review_id)
        if request.user == review.user:
            if request.method =="POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0 ):
                        error = "out of range, please leave a rating between 0 and 10"
                        return render(request, 'main/editreview.html', {"error": error, "form":form})
                    else:
                        data.save()
                        return redirect("main:detail", business_id)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'main/editreview.html', {"form" : form})
        else:
            return redirect("main:detail", business_id)
    else:
        return redirect("accounts:login")

def delete_review(request, business_id, review_id):
    if request.user.is_authenticated:
        business = Business.objects.get(id=business_id)
        review = Review.objects.get(business=business, id=review_id)
        if request.user == review.user:
            review.delete()
            return redirect("main:detail", business_id)
    else:
        return redirect("accounts:login")

