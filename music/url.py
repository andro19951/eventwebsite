from django.conf.urls import url

from . import views


urlpatterns = [
    # music/ index
    url(r'^$', views.index, name='index'),
    # /music/
    url(r'^(?P<album_id>[0-9]+)$', views.detail, name="events"),
]
