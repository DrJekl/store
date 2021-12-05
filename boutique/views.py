from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta, datetime
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import User, Comment, Listing
from .forms import RegistrationForm, CreateListing, DemandListing


# Create your views here.
def index(request):
	return render(request, "boutique/index.html", {
			"collection": Listing.objects.filter(available=True, buyer=None)
		})

def register(response):
	if response.method == "POST":
		form = RegistrationForm(response.POST)
		if form.is_valid:
			form.save()
		return redirect("index")
	form = RegistrationForm()
	return render(response, "registration/register.html", {
			"form": form
		})

def look(request, item):
	return render(request, "boutique/look.html", {
			"item": Listing.objects.get(name=item)
		})

@login_required
def create(request):
	if request.method == "POST":
		user = request.user
		if user.is_superuser:
			form = CreateListing(request.POST, request.FILES)
			if form.is_valid:
				listing = form.save(commit=False)
				listing.date = timezone.now()
				if not len(Listing.objects.filter(name=listing.name)):
					listing.save()
					return redirect("index")
		return render(request, "boutique/error.html")
	form = CreateListing()
	return render(request, "boutique/create.html", {
			"form": form
		})

@login_required
def demand(request):
	message = ""
	if request.method == "POST":
		user = request.user
		form = DemandListing(request.POST, request.FILES)
		if form.is_valid:
			listing = form.save(commit=False)
			listing.buyer = user
			if (len(Listing.objects.filter(name=listing.name, buyer=user.id)) > 0) or not listing.future2():
				message += "You have already requested this item!" * (len(Listing.objects.filter(name=listing.name, buyer=user.id)) > 0)
				message += "You have to pick a date in the future." * (not listing.future2())
				return render(request, "boutique/demand.html", {
						"form": form,
						"message": message
					})
			listing.save()
			return redirect("index")
	form = DemandListing()
	return render(request, "boutique/demand.html", {
			"form": form
		})

@login_required
def mystuff(request):
	user = request.user
	bought = Listing.objects.filter(buyer=user, available=False)
	demands = Listing.objects.filter(buyer=user, available=True)
	return render(request, "boutique/mystuff.html", {
			"bought": bought,
			"demands": demands
		})

def about(request):
	return render(request, "boutique/about.html")