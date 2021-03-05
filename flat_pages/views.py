from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from .models import Flat_Page
from images.models import Image
from django.contrib.auth.decorators import login_required


@login_required
def flat_page(request, slug):
    content = get_object_or_404(Flat_Page, slug=slug, active=True)
    links = get_list_or_404(Flat_Page, active=True)
    return render(request, 'flat_pages/flat_page.html',{'links':links,'content':content,})

