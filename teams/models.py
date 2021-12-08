from django.db import models

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from country.models import Country

def current_year():
    return datetime.date.today().year

#With this approach, this model will be included every makemigrations
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value) 

class Team(models.Model):
	full_name 		= models.CharField(max_length=150)
	name 			= models.CharField(max_length=100)
	nickname 		= models.CharField(max_length=100, blank=True, null=True)
	country			= models.ForeignKey(Country, on_delete=models.CASCADE)
	year_founded	= models.IntegerField(('year'), 
					  validators=[MinValueValidator(1850), max_value_current_year])
	stadium			= models.CharField(max_length=200)
	capacity		= models.IntegerField()
	owner			= models.CharField(max_length=150, blank=True)
	chairman		= models.CharField(max_length=150, blank=True)

	def __str__(self):
		return self.name + " (" + str(self.pk) + ")"
