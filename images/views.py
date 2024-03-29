from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from flat_pages.models import Flat_Page
from images.models import Image
from django.contrib.auth.decorators import login_required

@login_required
def pictures(request):
    links = Flat_Page.objects.filter(active=True).order_by('order') 
    pictures = Image.objects.filter(gallery=True).order_by('order') 
    return render(request, 'images/pictures.html',{'links':links,'pictures':pictures,})
