# solver/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bisection/', views.bisection, name='bisection'),
    path('newton_raphson/', views.newton_raphson, name='newton_raphson'),
    path('secant/', views.secant, name='secant'),
]
