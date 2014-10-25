from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    # router urls
    url(r'^', include(router.urls)),

    # blog urls
    url(r'^blog/', include('blog.urls')),

    # api urls
    url(r'^api/', include('rest_framework.urls', namespace='api')),

    # admin urls
    url(r'^admin/', include(admin.site.urls)),
]
