from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_view, name='my_view'),
]


