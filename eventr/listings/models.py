from django.db import models


# Have I used settings.py hard config values where the source might be defined here?
# I suppose depending on who's updating these sources, and how many there are (if there's a lot)
# I'm going to leave this with just this note....
class Source(models.Model): 
    spektrix_client_name = models.TextField(unique=True)
    friendly_name = models.TextField()
    default_city = models.CharField(max_length=200, null=True, blank=True)
    api_url = models.CharField(max_length=200, null=True, blank=True) # Derives from speaktrix client name, but full form URL seems good

    def __str__(self):
       return 'Source: ' + self.friendly_name

class Event(models.Model):
    source = models.ForeignKey(Source, related_name="events", on_delete=models.CASCADE)
    foreign_id = models.TextField(unique=True)
    name = models.TextField()
    duration_minutes = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

class EventInstance(models.Model):
    foreign_id = models.TextField()
    event = models.ForeignKey(Event, related_name="eventinstances", on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    venue_name = models.TextField(blank=True)
    venue_address = models.TextField(blank=True)


"""
I was in the middle of adding this, but since I'm just uploading what I've got right now, this breaks runtime

from listings.serializers import EventSerializer
class EventList(ListAPIView):
    queryset = Event.objects.all().filter()
    serializer_class = eventSerializer
    filter_backends = [DjangoFilterBackend] # NB: Is needed?
    filterset_fields = { 
        'start_datetime': ['date__range', 'gte', 'lte', 'exact', 'gt', 'lt']
    } 
    # NB: Worth googling these values to find where they are defined
    # in REST docs/code
    # Alternatively django-filter, but I think that's for the ORM

"""