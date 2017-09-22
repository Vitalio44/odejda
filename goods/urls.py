from django.conf.urls import url
from .views import main_page, update_data, category, get_update_data

urlpatterns = [
    url(r'^$', main_page, name="main"),
    url(r'^update/$', update_data, name="update"),
    url(r'^update/get_update$', get_update_data, name="get_update"),
    url(r'^(?P<slug>[-\w]+)/$', category, name="category"),
]
