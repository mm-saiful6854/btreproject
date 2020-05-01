from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def listings(request):
    return render(request,'listings/listings.html')


def listing(request):
    return render(request,'listings/listing.html')


def search(request):
    return render(request,'listings/search.html')