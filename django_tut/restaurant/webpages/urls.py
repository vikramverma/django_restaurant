from django.urls import path
from django.conf.urls import url
from . import views

app_name = "website"

urlpatterns = [
    # url(r'^dishes/(?P<dishes_type>[a-zA-Z]+)', views.menu, name='menu'),
    path('home', views.index, name='index'),
	path('contact-us', views.contact, name='contact-us'),
    #path('create_dish', views.create_dish, name='create_dish'),
    path('create_dish', views.store_dish, name='create_dish'),
    path('list_dish', views.list_dish, name='list_dish'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    # path('continental', views.continental, name='continental'),
    # path('indian', views.indian, name='indian'),
    # path('dishes/continental', views.menu, name='continental_menu'),
    # path('menu/indian', views.menu_indian, name='indian_menu'),
    # path('menu/chinese', views.menu_chinese, name='chinese_menu'),
    url(r'menu/(?P<type>[a-zA-Z]+)', views.menu, name='menu'),
    url(r'edit_dish/(?P<id>[0-9]+)', views.edit_dish, name='edit_dish'),
    url(r'delete_dish/(?P<id>[0-9]+)', views.delete_dish, name='delete_dish'),
    # url(r'dish/(?P<id>[0-9]+)', views.dish_page, name='dish_page')
    # path('dishes/indian', views.menu, name='indian_menu')
]