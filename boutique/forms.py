from django import forms
from django.forms.widgets import DateInput

from .models import User, Listing
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from datetime import timedelta, datetime


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
			"date": forms.DateInput(format="%d/%m/%Y", attrs={"placeholder": "DD/MM/YYYY"}),
		}


	
	def future(self):
		return self.date > timezone.now()

	def leap(self):
		year = int(self.date.strftime("%Y"))
		if year % 400 == 0:
			return True
		elif year % 4 == 0 and year % 100 != 0:
			return True
		return False

	def max_days(self):
		months = [i + 1 for i in range(12)]
		month = int(self.date.strftime("%m"))
		day = int(self.date.strftime("%d"))
		print("DAY: ", day, "  MONTH: ", month, sep=" ")
		if month not in months or day < 1:
			return False
		if month in [1, 3, 5, 7, 8, 10, 12]:
			if day > 31:
				return False
		elif month == 2:
			if self.leap():
				if day > 29:
					return False
			else:
				if day > 28:
					return False
		else:
			if day > 30:
				return False
		return True