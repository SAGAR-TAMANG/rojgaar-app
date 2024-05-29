from django.conf.urls.static import static
from ..main import settings
from django.urls import path
from .views import index, about, why, services, intro, assetlinks_json

urlpatterns = [
    path('', index),
    path('about', about),
    path('intro', intro),
    path('services', services),
    path('why', why),

    path('.well-known/assetlinks.json', assetlinks_json, name='assetlinks_json'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
