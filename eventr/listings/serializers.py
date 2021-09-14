from rest_framework.serializers import ModelSerializer
from .models import Event

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields=['foreign_id', 'name', 'duration_minutes', 'description']

# GTE / LTE / exact / gt / lt