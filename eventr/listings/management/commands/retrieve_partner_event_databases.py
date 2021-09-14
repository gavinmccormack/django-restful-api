import logging
import requests
from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.utils.text import slugify
from listings.models import Event, EventInstance, Source
from eventr.settings import PARTNER_CACHE_KEY_FORMAT, PARTNER_CACHE_TIME
from django import setup

logger = logging.getLogger('django.retrieve_partner_events')

def retrieve_partner_events(feed):
	cache_key = PARTNER_CACHE_KEY_FORMAT.format(slugify(feed.friendly_name))
	saved_json = cache.get(cache_key)
	if saved_json is not None:
		logger.info("Request to {} made recently, no updates made".format(feed.api_url))
		return saved_json

	# Make a request
	print(feed.api_url)
	r = requests.get(feed.api_url)
	if r.status_code == 200:
		cache.set(cache_key, r.json(), PARTNER_CACHE_TIME)
		print("Hurrah {} has results".format(feed))
		data = r.json()
		return data
	else:
		logger.warn("Feed retrieval for {} failed with status code {}".format(feed['url'], r.status_code))

def upload_events(events, source):
	""" Takes JSON object events, and database object source """
	# Get DB object for this source
	source_name = source.spektrix_client_name
	for event in events:
		external_api_id = event['id']
		name = event['name']
		duration = event['duration'] # What is running time?
		description = event['description'] # Description/html description - can't know which is relevant
		event_obj = Event.objects.get_or_create(source=source, foreign_id=external_api_id, name=name, duration_minutes=duration, description=description)
		
		# Instance times here like 9 - 10 may. I'm not clear on first/last instance time, the interval of shows, etc. 
		# For this I am just going to assume "firstInstanceDateTime" per entry is enough to handle eventInstances
		# Would confirm if this wasn't a demo project, but doesn't seem too important a detail.
		# Same goes for venue name and address. I'm not sure if it's implied that these would be part of the "source"
		# Or if the mapping of API val: DB value would vary based on the source.
		# Going to skip past
		start_datetime = event['firstInstanceDateTime'] venue_name = "Venue name"
		venue_address = "Address"
		event_instance = EventInstance.objects.get_or_create(foreign_id=external_api_id, event=event_obj[0], start_datetime=start_datetime, venue_name=venue_name, venue_address=venue_address)
		# Also for this, I thought the API would include some kind of unique ID for each event, but duplicate events for separate instances don't seem to share
		# anything that would make a good primary key for event objects
		# From here, just moving onto to DRF views instead of nitpicking the model:api relationship

class Command(BaseCommand):
	help = "Retrieves data from partner APIs and inserts them into the database"

	def handle(self, *args, **options):
		PARTNER_EVENT_APIS = Source.objects.all()
    	#print(PARTNER_EVENT_APIS[0].api_url)
		for feed in PARTNER_EVENT_APIS:
			events = retrieve_partner_events(feed)
			upload_events(events, feed)


# For toppingbooks there is a unique ID field. 