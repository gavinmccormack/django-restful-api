import logging
import requests
from django.core.management.base import BaseCommand
from eventr.settings import PARTNER_EVENT_APIS
from django.core.cache import cache
from django.utils.text import slugify

logger = logging.getLogger('django.retrieve_partner_events')

# NB: Do I need this
headers = {"User-Agent": '"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"'}


# So, I might split this into a download and an upload section as needed but.... as is it is does okay.
# I just use the cache here to check if the request was made recently
# but, depending on how often this command was run, and how often the data was updated
# you could do something like check the cache data hash against the request and then decide whether 
# it requires a DB update.
def retrieve_partner_events(feed):
	cache_key = PARTNER_CACHE_KEY.format(slugify(feed['url']))
	saved_json = cache.get(cache_key)
	if saved_json is None:
		logger.info("Request to {} made recently, no updates made")
		return

	# Make a request
	r = requests.get(feed['url'], headers=headers)
	if r.status_code == 200:
		cache.set(cache_key, r.json(), PARTNER_CACHE_TIME)
		print("Hurrah {} has results".format(feed))
		data = r.json()
	else:
		logger.warn("Feed retrieval for {} failed with status code {}".format(feed['url'], r.status_code))

class Command(BaseCommand):
    help = "Retrieves data from partner APIs and inserts them into the database"

    def handle(self, *args, **options):
    	for feed in PARTNER_EVENT_APIS:
    		retrieve_partner_events(feed)

# For toppingbooks there is a unique ID field. 