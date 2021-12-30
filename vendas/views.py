from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Vendas
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'vendas/index.html'
    context_object_name = 'listaVendas'
    def get_queryset(self):
        return Vendas.objects.all()
    
def NovaVenda(request):
    return HttpResponse("Nova venda")

def ExcluirVenda(request, id):
    try:
        venda = Vendas.objects.get(pk=id)
        venda.delete()
        return HttpResponseRedirect(reverse('vendas:index'))
    except Exception as e:
        return HttpResponseRedirect(reverse('produtos:index'))
def EditarVendaView(request, id):
    return HttpResponse("Nova venda")

def FinalizaEdittVendaView(request, id):
    return HttpResponse("Nova venda")