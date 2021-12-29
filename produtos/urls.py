from django.urls import path

from . import views

app_name = 'produtos'
urlpatterns = [
    path('/', views.IndexView.as_view(), name='index'),
    path('/cadastro/', views.CadastroProduto, name='cadastro')
]