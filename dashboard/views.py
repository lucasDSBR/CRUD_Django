from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
# Create your views here.

def IndexView(request):
    return HttpResponse("dashboard")