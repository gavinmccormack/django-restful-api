from rest_framework.serializers import ModelSerializer, RelatedField, CharField
from .models import Event, EventInstance, Source


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        fields = ["friendly_name", "default_city"]  # Default city + address


class EventSerializer(ModelSerializer):
    source = SourceSerializer(read_only=True)

    class Meta:
        model = Event
        fields = "__all__"


class EventInstanceSerializer(ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = EventInstance
        fields = "__all__"


# GTE / LTE / exact / gt / lt
# This is an event serializer, but if instances were correctly populated I would use that.
