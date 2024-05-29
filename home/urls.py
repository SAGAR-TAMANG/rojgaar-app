from django.urls import path
from .views import index, about, why, services, intro

urlpatterns = [
    path('', index),
    path('about', about),
    path('intro', intro),
    path('services', services),
    path('why', why),
]
