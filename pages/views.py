from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from realtors.models import Realtor
from listings.models import Listing
from listings.choice import price_choice,bedroom,state_choice



def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context ={
        'listings': listings,
        'state_choice': state_choice,
        'bedroom': bedroom,
        'price_choice': price_choice,
    }
    return render(request,'page/index.html',context)

def about(request):

    all_realtor = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : all_realtor,
        'mvp_realtors': mvp_realtors, 

    }

    return render(request,'page/about.html',context)