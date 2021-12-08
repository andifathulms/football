from django.db import models

from competition.models import Competition
from venue.models import Venue
from referee.models import Referee
from teams.models import Team

class Match(models.Model):
	competition 		= models.ForeignKey(Competition, on_delete=models.CASCADE)
	competition_phase 	= models.CharField(max_length=150)
	date 				= models.DateTimeField()
	venue 				= models.ForeignKey(Venue, on_delete=models.CASCADE)
	referee 			= models.ForeignKey(Referee, on_delete=models.CASCADE)
	home_team			= models.ForeignKey(Team, on_delete=models.CASCADE)
	away_team			= models.ForeignKey(Team, on_delete=models.CASCADE)
	home_score			= models.IntegerField()
	away_score			= models.IntegerField()
	home_score_ET		= models.IntegerField(blank=True, null=True)
	away_score_ET		= models.IntegerField(blank=True, null=True)
	home_score_PK		= models.IntegerField(blank=True, null=True)
	awat_score_PK		= models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.home_team + "-" + self.away_team + self.competition + " " + self.competition_phase