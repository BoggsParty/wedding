from django.db import models

class Documents(models.Model):
    title = models.CharField(max_length=200, default='', unique=True, blank=True)
    description = models.TextField(default='',blank=True)
    document = models.FileField(upload_to = 'filestorage/')
    
    def __str__(self):
        return self.title