from django.urls import path
from .views import index, about, why, services, intro, assetlinks_json

urlpatterns = [
    path('', index),
    path('about', about),
    path('intro', intro),
    path('services', services),
    path('why', why),

    path('.well-known/assetlinks.json', assetlinks_json, name='assetlinks_json'),
]
