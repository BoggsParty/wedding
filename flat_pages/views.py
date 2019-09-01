from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Flat_Page
from django.contrib.auth.decorators import login_required

@login_required
def flat_page(request, slug):
    content = get_object_or_404(Flat_Page, slug=slug)
    links = get_list_or_404(Flat_Page)
    return render(request, 'flat_pages/flat_page.html',{'links':links,'content':content,})
