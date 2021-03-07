from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from flat_pages.models import Flat_Page
from images.models import Image
from django.contrib.auth.decorators import login_required
from .forms import RSVPForm

@login_required
def rsvp(request):
    links = Flat_Page.objects.filter(active=True).order_by('order')
    if request.method == "POST":
        form = RSVPForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('thank_you')
    else:
        form = RSVPForm()
    return render(request, 'guests/rsvp.html', {'form': form,'links':links,})

@login_required  
def thank_you(request):
    links = Flat_Page.objects.filter(active=True).order_by('order')
    return render(request, 'guests/thank_you.html',{'links':links,})