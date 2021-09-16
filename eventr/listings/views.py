from django.shortcuts import render
from listings.serializers import EventSerializer
from listings.models import Event
from django.http import HttpResponse, JsonResponse

def listings(request):
	context = {}
	return render(request, 'index.html', context) 

def events_view(request):
	# Okay, so because it's neater to have something that works.
	# And the data isn't too large, I'm going to skip
	# using the filtering/queryset aspect of events
	# Up to a reasonable point, a lot of filtering 
	# can be done on the user side.
	# Usually text based JSON data is minor,
	# and you can have a really fast search function
	# if the logic is userside.
	events = Event.objects.all()
	serializer = EventSerializer(events, many=True)
	return JsonResponse(serializer.data, safe=False)