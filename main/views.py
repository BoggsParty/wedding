from django.shortcuts import render, get_list_or_404
from django.http import Http404
from flat_pages.models import Flat_Page
from guests.models import Guest
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required(login_url='/accounts/login/') 
def main(request):
    links = Flat_Page.objects.filter(active=True).order_by('order')
    return render(request, 'main/home.html',{'links':links,})
    
    
@login_required   
def totals(request):
    if request.user.is_staff:
        pass
    else:
        raise Http404
        
    links = Flat_Page.objects.filter(active=True).order_by('order')
    welcome_party_total = Guest.objects.aggregate(total=Sum('rsvp_welcome_dinner'))['total']
    boat_total = Guest.objects.aggregate(total=Sum('rsvp_boat'))['total']
    invited = Guest.objects.aggregate(total=Sum('total_guests'))['total']
    expected = Guest.objects.aggregate(total=Sum('expected_guests'))['total']
    
    return render(request, 'main/totals.html',{'links':links,'welcome_party_total':welcome_party_total,'boat_total':boat_total,'invited':invited, 'expected':expected,})
