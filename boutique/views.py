from django.shortcuts import render, redirect
from django.utils import timezone
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
				listing.save()
				return redirect("look", listing.name)
			else:
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
			if listing.date <= timezone.now():
				message = "You have to pick a date in the future!"
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