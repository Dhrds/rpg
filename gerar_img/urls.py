from django.urls import path
from . import views


urlpatterns = [
    path('gerar-img/', views.gera_img, name='gerar_img'),
]