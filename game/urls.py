from django.urls import path

from . import views

urlpatterns = [
    path('aventura/', views.jogo_rpg, name='aventura'),
    path('', views.home, name='home'),
]