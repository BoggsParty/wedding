from django.db import models

class Guest (models.Model):

    name = models.CharField(max_length=100)
    additional_guests = models.TextField(max_length=1000, blank=True)
    total_guests = models.IntegerField(default=0)
    address = models.TextField(max_length=1000)
    phone = models.CharField(max_length=100, blank=True)
    no_std = models.BooleanField(default=False)
    STD_sent = models.DateField(auto_now=False, blank=True)
    invitation_sent = models.DateField(auto_now=False, blank=True)
    welcome_dinner_invite = models.BooleanField(default=False)
    party_invite = models.BooleanField(default=False)
    rsvp_welcome_dinner = models.IntegerField(default=0)
    rsvp_boat = models.IntegerField(default=0)
    rsvp_party = models.IntegerField(default=0)
    notes = models.TextField(max_length=1000, blank=True)
        
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.name
