from django.db import models

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

from cup.models import Cup
from country.models import Country

def current_year():
    return datetime.date.today().year

#With this approach, this model will be included every makemigrations
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value) 

class League(models.Model):
	title               = models.CharField(max_length=150)
	organising_body     = models.CharField(max_length=150)
	year             	= models.IntegerField(('year'), 
					  	  validators=[MinValueValidator(1850), max_value_current_year])
	country             = models.ForeignKey(Country, on_delete=models.CASCADE)
	confederation       = models.CharField(max_length=100)
	level               = models.IntegerField()
	relegation_to       = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
	domestic_cup        = models.ManyToManyField(Cup, blank=True, related_name='domestic_cup')
	league_cup          = models.ManyToManyField(Cup, blank=True, related_name='league_cup')
	international_cup   = models.ManyToManyField(Cup, blank=True, related_name='international_cup')

	def __str__(self):
		return self.title + " (" + str(self.pk) + ")"