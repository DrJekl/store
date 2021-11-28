from django import forms

from .models import User, Listing
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "password1", "password2", "email")

		widgets = {
			"username": forms.TextInput(attrs={"class": "form-control"}),
			"password1": forms.PasswordInput(attrs={"class": "form-control"}),
			"password2": forms.PasswordInput(attrs={"class": "form-control"}),
			"email": forms.EmailInput(attrs={"class": "form-control"}),
		}

class CreateListing(forms.ModelForm):
	class Meta:
		model = Listing
		fields = ("category", "name", "pic", "description", "price")

		widgets = {
			"category": forms.Select(attrs={"class": "form-control"}),
			"name": forms.TextInput(attrs={"class": "form-control"}),
			"pic": forms.FileInput(attrs={"class": "form-control"}),
			"description": forms.Textarea(attrs={"class": "form-control"}),
			"price": forms.NumberInput(attrs={"class": "form-control"}),
		}

class DemandListing(forms.ModelForm):
	class Meta:
		model = Listing
		fields = ("category", "name", "pic", "description", "price", "date")

		widgets = {
			"category": forms.Select(attrs={"class": "form-control"}),
			"name": forms.TextInput(attrs={"class": "form-control"}),
			"pic": forms.FileInput(attrs={"class": "form-control"}),
			"description": forms.Textarea(attrs={"class": "form-control"}),
			"price": forms.NumberInput(attrs={"class": "form-control"}),
			"date": forms.DateInput(attrs={"placeholder": "DD/MM/YYYY"}),
		}