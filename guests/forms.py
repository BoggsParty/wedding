from django import forms
from .models import RSVP

class RSVPForm(forms.ModelForm):

    class Meta:
        model = RSVP
        fields = ('guests', 'rsvp', 'email','vaccinated','notes',)