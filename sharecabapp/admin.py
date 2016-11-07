from django.contrib import admin

# Register your models here.
from .models import Ride

#class PersonInline(admin.TabularInline):
 #   model = Person
 #  extra = 1


class RideAdmin(admin.ModelAdmin):
    #inlines = [PersonInline]
    list_display = ('name','destination', 'source', 'ridedate','ridetime','preference','train','email')
    list_filter = ['ridetime']
    search_fields = ['destination','source']

admin.site.register(Ride, RideAdmin)
#admin.site.register(Person)
