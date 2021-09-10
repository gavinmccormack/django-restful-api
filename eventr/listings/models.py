from django.db import models

class Source(models.Model):
    spektrix_client_name = models.TextField(unique=True)
    friendly_name = models.TextField()

class Event(models.Model):
    source = models.ForeignKey(Source, related_name="events", on_delete=models.CASCADE)
    foreign_id = models.TextField()
    name = models.TextField()
    duration_minutes = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

class EventInstance(models.Model):
    foreign_id = models.TextField()
    event = models.ForeignKey(Event, related_name="instances", on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    venue_name = models.TextField(blank=True)
    venue_address = models.TextField(blank=True)