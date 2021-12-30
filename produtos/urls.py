from django.urls import path

from . import views

app_name = 'produtos'
urlpatterns = [
    path('/', views.IndexView.as_view(), name='index'),
    path('/novoProduto/', views.NovoProduto, name='novoProduto'),
    path('/cadastro/', views.CadastroProduto, name='cadastro'),
    path('/<int:id>/excluir', views.EcluirProduto, name='excluir'),
    path('/<int:id>/editar', views.EditartProdView, name='editar'),
    path('/<int:id>/finalizaEdicao', views.FinalizaEdittProdView, name='finalizaredicao')
]