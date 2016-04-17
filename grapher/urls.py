from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.graph_test, name='graph_test'),
]
