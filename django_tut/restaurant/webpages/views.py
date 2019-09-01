from django.shortcuts import render, HttpResponse, render_to_response
from webpages.models import Dish
import datetime

# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')

def contact(request):
    phone_no = "0120-1234567"
    return render(request=request, template_name='contact-us.html', context={'phone_no':phone_no})

# def continental(request):
#     menu=["sandwitches", "pasta", "burgers"]
#     return render(request=request, template_name='menu.html', context={'menu_items':menu})

# def menu_indian(request):
#     menu = ["dal roti", "chole bhatuure", "aalu puri"]
#     return render(request=request, template_name='menu.html', context={'menu_items':menu})
#
# def menu_chinese(request):
#     menu = ["noodles"]
#     return render(request=request, template_name='menu.html', context={'menu_items': menu})

# def menu(request, type):
#     # type = request.GET['type']
#     if type == "indian":
#         indian_menu = Dish.objects.filter(category="indian")
#         menu = []
#         for item in indian_menu:
#             item_name = item.name
#             menu.append(item_name)
#
#         # menu = [item.name for item in indian_menu]
#
#         # menu = ["dal roti", "chole bhatuure", "aalu puri"]
#     elif type == "continental":
#         menu = ["sandwitches", "pasta", "burgers"]
#     elif type == "chinese":
#         menu = ["noodles"]
#     else:
#         menu = []
#     return render(request=request, template_name='menu.html', context={'menu_items': menu})

def menu(request, type):
    # type = request.GET['type']
    if type == "indian":
        menu = Dish.objects.filter(category="indian", rate__lte = 50)
    elif type == "continental":
        menu = Dish.objects.exclude(category="indian")
    elif type == "chinese":
        menu = Dish.objects.filter(category="chinese")
    else:
        menu = []
    return render(request=request, template_name='menu.html', context={'menu_items': menu})


def create_dish(request):
    # my_dish = Dish(name="pani puri", image="pani_puri.jpeg")
    # my_dish.rate = 20.00
    # my_dish.available_from = datetime.datetime.now()
    # my_dish.category = "indian"
    # my_dish.isVeg = True
    # my_dish.is_available = True
    # my_dish.save()
    return HttpResponse("dish created here")

# def dish_page(request, id):
#     return HttpResponse(id)