from django.contrib import admin
from .models import Source, Event, EventInstance 

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(EventInstance)
class EventInstanceAdmin(admin.ModelAdmin):
    pass

