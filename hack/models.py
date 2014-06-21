from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    link = models.URLField()
    # image = models.ImageField(upload_to='image/%Y/%m/%d')

class Recommendation(models.Model):
    resources = models.ManyToManyField(Resource, related_name='recommendation', null=True, default=[])
    num_volunteers = models.IntegerField(null=False)

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='events/%Y/%m/%d')
    recommendation_1 = models.ForeignKey(Recommendation, null=True, blank=True, related_name='event_1')
    recommendation_2 = models.ForeignKey(Recommendation, null=True, blank=True, related_name='event_2')
    recommendation_3 = models.ForeignKey(Recommendation, null=True, blank=True, related_name='event_3')
    resources = models.ManyToManyField(Resource, related_name='event', null=True, default=[])

class Survey(models.Model):
    resources_used = models.ManyToManyField(Resource, related_name='survey', null=True, default=[])
    rating = models.IntegerField(null=False)
    event = models.ForeignKey(Event, related_name='survey_event')