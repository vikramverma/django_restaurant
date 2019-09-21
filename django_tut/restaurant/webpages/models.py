from django.db import models
import datetime
# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=50)
    rate = models.FloatField()
    isVeg = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    image = models.TextField(null = True)
    available_from = models.DateTimeField(default=datetime.datetime.now())
    is_available = models.BooleanField()


class Order(models.Model):
    order = models.TextField()
    mobile = models.TextField()

    def __str__(self):
        return self.order + " - " +self.mobile

class Dish_category(models.Model):
    category_name = models.TextField()

    def __str__(self):
        return self.category_name

class admin_user(models.Model):
    username = models.CharField(max_length=250)
    password = models.TextField()

class Discount(models.Model):
    discount_value = models.FloatField()
    discount_on = models.ForeignKey(Dish, on_delete=models.CASCADE)


class PromoCode(models.Model):
    code = models.TextField()
    valid_till = models.DateField()
