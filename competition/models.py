from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Competition(models.Model):
	
	season			= models.ForeignKey('Season', on_delete=models.CASCADE)
	date_started	= models.DateTimeField(blank=True, null=True)
	date_end		= models.DateTimeField(blank=True, null=True)
	no_competitor	= models.IntegerField()

	#Content Type model
	limit 			= models.Q(app_label = 'league', model = 'league') | models.Q(app_label = 'cup', model = 'cup')
	content_type 	= models.ForeignKey(ContentType, limit_choices_to = limit, on_delete=models.CASCADE)
	object_id 		= models.PositiveIntegerField()
	content_object  = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.season.title + " " + self.content_object.title

class Season(models.Model):
	title	= models.CharField(max_length=100)

	def __str__(self):
		return self.title
