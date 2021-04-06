from django.db import models

class Guest (models.Model):

    guest_1 = models.CharField(max_length=100)
    guest_2 = models.CharField(max_length=100, blank=True)
    kids = models.CharField(max_length=100, blank=True)
    total_guests = models.IntegerField(default=0)
    expected_guests = models.IntegerField(default=0)
    rsvp_guests = models.IntegerField(default=0)
    
    address = models.TextField(max_length=1000, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    
    welcome_dinner_invite = models.BooleanField(default=False)
    rsvp_welcome_dinner = models.BooleanField(default=False)
    vaccinated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.guest_1

class RSVP (models.Model):

    guests = models.CharField(max_length=500, blank=True)
    
    BOOL_CHOICES = ((True, 'Accepts with pleasure'), (False, 'Declines with regret'))
    rsvp = models.BooleanField(choices=BOOL_CHOICES,default=False)
    
    email = models.EmailField(blank=True)
    notes = models.TextField(max_length=1000,blank=True)
    