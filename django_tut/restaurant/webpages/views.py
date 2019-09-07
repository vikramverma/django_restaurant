from django.shortcuts import render, HttpResponse, render_to_response
from webpages.models import Dish
from django.conf import settings
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


def store_dish(request):
    status  = 'Create a dish here'
    if request.POST:
        name = request.POST['name']
        category = request.POST['category']
        rate = request.POST['rate']
        rate = float(rate)
        available_from = request.POST['available_from']
        available_from = datetime.datetime.strptime(available_from, '%Y-%m-%d').date()
        is_veg = True if 'is_veg' in request.POST else False
        is_available = True if 'is_available' in request.POST else False
        file = request.FILES['file']
        dest_file = settings.BASE_DIR + '/static/images/'+file.name
        with open(dest_file,'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        dish = Dish(name=name, category = category, rate = rate, available_from = available_from, isVeg = is_veg, is_available = is_available, image = file.name)
        dish.save()
        status = 'Dish Added!'
    return render(request=request, template_name='store_dish.html', context={'status':status})