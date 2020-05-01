from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>realtors</h1>")

def realtor(request):
    return HttpResponse("<h1>realtor</h1>")