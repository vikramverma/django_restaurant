from django.urls import path
from django.conf.urls import url
from . import views

app_name = "website"

urlpatterns = [
    # url(r'^dishes/(?P<dishes_type>[a-zA-Z]+)', views.menu, name='menu'),
    path('home', views.index, name='index'),
	path('contact-us', views.contact, name='contact-us'),
    # path('continental', views.continental, name='continental'),
    # path('indian', views.indian, name='indian'),
    # path('dishes/continental', views.menu, name='continental_menu'),
    # path('menu/indian', views.menu_indian, name='indian_menu'),
    # path('menu/chinese', views.menu_chinese, name='chinese_menu'),
    url(r'menu/(?P<type>[a-zA-Z]+)', views.menu, name='menu')
    # path('dishes/indian', views.menu, name='indian_menu')
]