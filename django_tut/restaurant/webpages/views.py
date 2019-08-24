from django.shortcuts import render, HttpResponse, render_to_response

# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')

def contact(request):
    phone_no = "0120-1234567"
    return render(request=request, template_name='contact-us.html', context={'phone_no':phone_no})

def continental(request):
    menu=["sandwitches", "pasta", "burgers"]
    return render(request=request, template_name='menu.html', context={'menu_items':menu})

def indian(request):
    menu = ["dal roti", "chole bhatuure", "aalu puri"]
    return render(request=request, template_name='menu.html', context={'menu_items':menu})

def menu(request):
    if request.GET['type'] == "indian":
        menu = ["dal roti", "chole bhatuure", "aalu puri"]
    elif request.GET['type'] == "continental":
        menu = ["sandwitches", "pasta", "burgers"]
    else:
        menu = []
    return render(request=request, template_name='menu.html', context={'menu_items': menu})