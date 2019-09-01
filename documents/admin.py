from django.contrib import admin
from .models import Documents

class documents_admin(admin.ModelAdmin):
    #list_display = ('title') 
    pass
    
admin.site.register(Documents,documents_admin)