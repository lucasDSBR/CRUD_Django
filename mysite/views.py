from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from produtos.models import Produtos

# Create your views here.

def Index(request):
    return render(request, 'dashboard/index.html')
