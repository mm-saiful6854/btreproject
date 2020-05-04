from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Listing
from django.core.paginator import Paginator

from .choice import price_choice,bedroom,state_choice

# Create your views here.


def listings(request):

    all_listing = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(all_listing,4)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number) 



    context ={
        'listings' : paged_listings,
    }
    return render(request,'listings/listings.html',context)


def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context= {
        'list': listing,
    }
    return render(request,'listings/listing.html',context)


def search(request):

    list = Listing.objects.order_by('-list_date').filter(is_published=True)

    #keywords
    if('keywords' in request.GET):
        keywords = request.GET["keywords"]
        if(keywords):
            list = list.filter(description__icontains=keywords)


    #city
    if('city' in request.GET):
        city = request.GET["city"]
        if(city):
            list = list.filter(city__iexact=city)
    

    #state
    if('state' in request.GET):
        state = request.GET["state"]
        if(state):
            list = list.filter(state__iexact=state)
    
   #bedrooms
    if('bedrooms' in request.GET):
        bedrooms = request.GET["bedrooms"]
        if(bedrooms):
            list = list.filter(bedrooms__lte=bedrooms) 

      
   #price
    if('price' in request.GET):
        price = request.GET["price"]
        if(price):
            list = list.filter(price__lte=price) 

    context={
        'state_choice': state_choice,
        'bedroom': bedroom,
        'price_choice': price_choice,
        'listings': list
    }

    return render(request,'listings/search.html',context)