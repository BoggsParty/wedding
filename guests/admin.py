from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Guest

class guest_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display  = ('name','total_guests','address',)
    list_filter = ('rsvp_boat',)
    search_fields = ('name',)

admin.site.register(Guest,guest_admin,)

class GuestResource(resources.ModelResource):
    class Meta:
        model = Guest
