from django.contrib import admin
from .models import Flight, Airports, Passengers 

class FlightAdmin(admin.ModelAdmin):
	list_display = ("id", "origin", "destination", "duration")


admin.site.register(Flight, FlightAdmin)
admin.site.register(Airports)
admin.site.register(Passengers)

# Register your models here.
