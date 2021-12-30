from django.urls import path

from . import views

app_name = 'vendas'
urlpatterns = [
    path('/', views.IndexView.as_view(), name='index'),
    path('/novaVenda/', views.NovaVenda, name='novaVenda'),
    path('/<int:id>/excluir', views.ExcluirVenda, name='excluir'),
    path('/<int:id>/editar', views.EditarVendaView, name='editar'),
    path('/<int:id>/finalizaEdicao', views.FinalizaEdittVendaView, name='finalizaredicao')
]