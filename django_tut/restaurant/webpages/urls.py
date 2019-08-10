from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('home', views.index, name='index'),
	url(r'^$', views.index, name='index'),
    path('contact-us', views.contact, name='index'),
]