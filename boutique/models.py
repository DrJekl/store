from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime

# Create your models here.
class User(AbstractUser):
	watching = models.ManyToManyField("Listing", blank=True)

	def __str__(self):
		return f"{self.username}"

class Comment(models.Model):
	author = models.ForeignKey("User", on_delete=models.CASCADE)
	about = models.ForeignKey("Listing", on_delete=models.CASCADE)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Comment by {self.author} on {self.date}"

class Listing(models.Model):
	categories = [
		("mens", "Mens"),
		("womens", "Womens"),
		("girls", "Girls"),
		("boys", "Boys"),
		("kids", "Kids")
	]
	category = models.CharField(max_length=8, choices=categories)
	name = models.CharField(max_length=32)
	pic = models.ImageField(upload_to="images/", null=True, blank=True)
	description = models.CharField(max_length=256, null=True, blank=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	date = models.DateTimeField(null=True, blank=True)
	buyer = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True)
	available = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.name} for {self.price}"

	def future2(self):
		return datetime.strftime(self.date, "%m/%d/%Y") > datetime.strftime(timezone.now(), "%d/%m/%Y")