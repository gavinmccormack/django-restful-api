from django.shortcuts import render
from listings.serializers import EventInstanceSerializer
from listings.models import EventInstance  # NB: Can remove Event if inst based
from django.http import JsonResponse
from rest_framework.views import APIView
from datetime import datetime, timedelta


def listings(request):
    context = {}
    return render(request, "index.html", context)


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class EventApi(APIView):
    # Unfamiliar with the APIView class. Could be doing all kinds of things.
    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, format=None):
        if request.GET.get("today"):
            today = datetime.now()
            tomorrow = datetime.now() + timedelta(
                days=100
            )  # For a certain definition of today
            events = EventInstance.objects.filter(
                start_datetime__range=[today, tomorrow]
            ) 
            events = events.select_related("event", "event__source")
            serializer = EventInstanceSerializer(events, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            events = EventInstance.objects.all().select_related(
                "event", "event__source"
            )
            serializer = EventInstanceSerializer(events, many=True)
            return JsonResponse(serializer.data, safe=False)
