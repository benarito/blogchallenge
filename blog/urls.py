from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    # urls
    url(r'^', ListPosts.as_view(), name='list'),
)