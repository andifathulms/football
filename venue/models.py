from django.db import models

class Venue(models.Model):
	name 	 		 = models.CharField(max_length=200)
	capacity 		 = models.IntegerField()
	location 		 = models.CharField(max_length=200)
	location_city    = models.CharField(max_length=200)
	location_country = models.CharField(max_length=200)

	def __str__(self):
		return self.name
