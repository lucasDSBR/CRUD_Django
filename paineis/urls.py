from django.urls import path

from . import views

app_name = 'paineis'
urlpatterns = [
    path('/', views.IndexView, name='index')
]