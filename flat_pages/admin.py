from django.contrib import admin
from .models import Flat_Page
#from django_summernote.admin import SummernoteModelAdmin


class flat_page_admin(admin.ModelAdmin):
    list_display = ('title','slug')
    prepopulated_fields = {"slug": ("title",)}
    #sumernote_fields = '__all__'
    
    
admin.site.register(Flat_Page,flat_page_admin)
