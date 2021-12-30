from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from vendas.models import Vendas
from produtos.models import Produtos
import plotly.graph_objects as go
import pandas as pd
# Create your views here.


def IndexView(request):
    estados = []
    vends = Vendas.objects.all()
    for i in vends:
        estados.append(i.venda_estado_destino)
    df = pd.DataFrame({'Estados': estados})
    a = df['Estados'].unique()
    b = df['Estados'].value_counts()
    fig = go.Figure(
        data=[go.Bar(y=b, x=a)],
        layout_title_text="Total de vendas por região"
    )
    
    mes = [' --- ','janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    meses = []
    for i in vends:
        a = i.venda_Data
        b = mes[a.month]
        meses.append(b)
    
    dfMeses = pd.DataFrame({'Meses': meses})
    d = dfMeses['Meses'].unique()
    c = dfMeses['Meses'].value_counts()
    figMes = go.Figure(
        data=[go.Bar(y=c, x=d)],
        layout_title_text="Total de vendas por mês"
    )
    
    return render(request, 'paineis/index.html', 
                  {
                      'graficoVendasRegiao': fig.to_html(), 
                      'graficoVendasMes': figMes.to_html(),
                   })