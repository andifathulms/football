from django.db import models

class Country(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Region(models.Model):
	name = models.CharField(max_length=150)
	country = models.ManyToManyField("Country")

	def __str__(self):
		return self.name
