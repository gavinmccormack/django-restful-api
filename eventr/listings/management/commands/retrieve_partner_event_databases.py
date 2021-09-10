import logging
import requests
from django.core.management.base import BaseCommand
from eventr.settings import PARTNER_EVENT_APIS

logger = logging.getLogger('django.retrieve_partner_events')

class Command(BaseCommand):
    help = "Retrieves data from partner APIs and inserts them into the database"

    def handle(self, *args, **options):
    	print("PARTNER EVENT APIS")
    	for feed in PARTNER_EVENT_APIS:
    		r = requests.get(feed)
    		if r.status_code == 200:
    			print("Hurrah {} has results".format(feed))
    		else:
    			logger.warn("Feed retrieval for {} failed with status code {}".format(feed, r.status_code))
