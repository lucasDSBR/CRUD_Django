from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Produtos
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'produtos/index.html'
    context_object_name = 'listaProdutos'
    def get_queryset(self):
        return Produtos.objects.all()
def NovoProduto(request):
     return render(request, 'produtos/novoProduto.html')
 
def CadastroProduto(request):
    try:
        prod = Produtos(
            prod_Nome = request.POST['nome'],
            prod_Codigo = int(request.POST['codigo']),
            prod_Preco = float(request.POST['preco']),
            prod_Fornecedor = int(request.POST['fornecedor']),
            prod_Total_estoque = int(request.POST['total_estoque'])
            )
        prod.save()
        template_name = 'produtos/index.html'
        context_object_name = 'listaProdutos'
        return HttpResponseRedirect(reverse('produtos:index'))
    except Exception:
        return render(request, 'produtos/index.html', {'error_message': 'Erro ao enviar os dados.'})

def EcluirProduto(request, id):
    try:
        produto = Produtos.objects.get(pk=id)
        produto.delete()
        return HttpResponseRedirect(reverse('produtos:index'))
    except Exception:
        return render(request, 'produtos/index.html', {'produto': produto, 'error_message': "Erro ao excluir o item." })

def EditartProdView(request, id):
    produto = Produtos.objects.get(pk=id)
    return render(request, 'produtos/editar.html', {'produto': produto})

def FinalizaEdittProdView(request, id):
    try:
        produto = Produtos.objects.get(pk=id)
        produto.prod_Nome=request.POST['nome']
        produto.prod_Codigo=int(request.POST['codigo'])
        produto.prod_Preco=float(request.POST['preco'])
        produto.prod_Total_estoque=int(request.POST['total_estoque'])
        produto.prod_Fornecedor=int(request.POST['fornecedor'])
        produto.save()
        return HttpResponseRedirect(reverse('produtos:index'))
    except Exception as e:
        return HttpResponseRedirect(reverse('produtos:index'))