from django.db import models

from teams.models import Team
from country.models import Country

class Manager(models.Model):
	name 			= models.CharField(max_length=150)
	date_of_birth	= models.DateTimeField(blank=True, null=True)
	nationality		= models.ForeignKey(Country, on_delete=models.CASCADE)
	height			= models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.name + " (" + str(self.pk) + ")"

class ManagerReign(models.Model):
	manager 		= models.ForeignKey('Manager', on_delete=models.CASCADE)
	date_from 		= models.DateTimeField()
	date_to 		= models.DateTimeField(blank=True, null=True)
	team 			= models.ForeignKey(Team, on_delete=models.CASCADE)
	status			= models.CharField(default="Manager", max_length=100)
	is_current		= models.BooleanField(default=True)

	def __str__(self):
		return self.manager.name + " - " + self.team.name + " (" + str(self.pk) + ")"
