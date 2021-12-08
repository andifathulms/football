from django.db import models

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

from country.models import Region

def current_year():
    return datetime.date.today().year

#With this approach, this model will be included every makemigrations
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value) 

class Cup(models.Model):
	title           = models.CharField(max_length=150)
	status          = models.CharField(max_length=150)
	region          = models.ForeignKey(Region, on_delete=models.CASCADE)
	organising_body = models.CharField(max_length=150)
	year            = models.IntegerField(('year'), 
					  validators=[MinValueValidator(1850), max_value_current_year])

	def __str__(self):
		return self.title + " (" + str(self.pk) + ")"