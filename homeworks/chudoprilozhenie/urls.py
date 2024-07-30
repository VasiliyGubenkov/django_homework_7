from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first_view, name='first_view'),
    path('second/', views.second_view, name='second_view'),
]