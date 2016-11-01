from django.contrib import admin

# Register your models here.
from .models import Ride, Person

class PersonInline(admin.TabularInline):
    model = Person
    extra = 1


class RideAdmin(admin.ModelAdmin):
    inlines = [PersonInline]
    list_display = ('destination', 'source', 'ridetime', 'capacity')

admin.site.register(Ride, RideAdmin)
#admin.site.register(Person)
