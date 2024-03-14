from django.contrib import admin

from .models import Airport, Flight, Passenger


class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Airport)