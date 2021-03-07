from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True)
    image = models.ImageField()
    gallery = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title