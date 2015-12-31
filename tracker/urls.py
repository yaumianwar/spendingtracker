from django.conf.urls import url

from .views import index as indexTracker

urlpatterns = [
               url(r'^$', indexTracker, name='index'),
               ]