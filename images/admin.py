from django.contrib import admin
from .models import Image

class image_admin(admin.ModelAdmin):
    list_display  = ('title',)

admin.site.register(Image,image_admin,)

