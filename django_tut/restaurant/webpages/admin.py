from django.contrib import admin
from .models import PromoCode, Dish, Discount, Dish_category, Order
# Register your models here.
admin.site.register(PromoCode)
admin.site.register(Discount)
admin.site.register(Dish)
admin.site.register(Dish_category)
admin.site.register(Order)