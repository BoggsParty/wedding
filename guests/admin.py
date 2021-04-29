from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Guest, RSVP

class guest_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display  = ('guest_1','rsvp','rsvp_guests','address','vaccinated')
    search_fields = ('guest_1',)
    list_filter = ('rsvp',)

admin.site.register(Guest,guest_admin,)

class GuestResource(resources.ModelResource):
    class Meta:
        model = Guest

class rsvp_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display  = ('guests',)

admin.site.register(RSVP,rsvp_admin,)

class GuestResource(resources.ModelResource):
    class Meta:
        model = RSVP