from django.db import models


# Create your models here.

class MyUser(models.Model):
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	email = models.EmailField()
	user_age = models.IntegerField()

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
