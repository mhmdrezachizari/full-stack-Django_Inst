from django.urls import include, path
from django.contrib import admin
from django.urls import path
from .views import post_list
from django.conf import settings
from django.conf.urls.static import static
app_name = 'blogtechnology'
urlpatterns = [
path('',post_list , name="list"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)