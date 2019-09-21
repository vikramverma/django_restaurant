from django.shortcuts import render, HttpResponse, render_to_response, redirect
from webpages.models import Dish, admin_user, Dish_category, Order
from django.conf import settings
from django.core.mail import send_mail
import datetime, json

# Create your views here.
def index(request):
    is_admin = check_admin(request)
    return render(request=request, template_name='index.html', context={'admin_menu':is_admin})

def contact(request):
    phone_no = "0120-1234567"
    is_admin = check_admin(request)
    if request.POST:
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        message = request.POST['message']
        message_subject = "Message from our site"
        message_body = "Name: " + name + " Mobile:" + mobile + " EMail:" + email + " Message:" + message
        send_mail(from_email='from_email', recipient_list=['admin@company_mail.com'], subject=message_subject, message = message_body)
    return render(request=request, template_name='contact-us.html', context={'phone_no':phone_no, 'admin_menu':is_admin})

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

def search(request):
    search = request.GET.get('search', None)
    if search is not None:
        menu = Dish.objects.filter(name__icontains = search)
    else:
        menu = []
    # is_admin = check_admin(request)
    # return render(request=request, template_name='menu.html', context={'menu_items': menu, 'admin_menu': is_admin})
    menu_items = []
    for item in menu:
        menu_items.append({
            'name':item.name,
            'rate':item.rate,
            'image':item.image
        })
    return HttpResponse(json.dumps(menu_items))

def menu(request, type):
    search = request.GET.get('search', None)
    # type = request.GET['type']
    if search is not None:
        menu = Dish.objects.filter(name__icontains = search)
    else:
        if type == "indian":
            menu = Dish.objects.filter(category="indian")
        elif type == "continental":
            menu = Dish.objects.exclude(category="indian")
        elif type == "chinese":
            menu = Dish.objects.filter(category="chinese")
        else:
            menu = []
    is_admin = check_admin(request)
    if request.POST:
        selections = request.POST.getlist('selection')
        qtys = request.POST.getlist('qty')
        order = []
        count = len(selections)
        for i in range(0, count):
            this_dish = Dish.objects.get(id=selections[i])
            qty = qtys[i]
            order.append(this_dish.name+" - " +str(qty))
        # for item in selections:
        #     this_dish = Dish.objects.get(id = item)
        #     order.append(this_dish.name)
        order = ", ".join(order)
        mobile = request.POST['mobile']

        Order(mobile = mobile, order = order).save()

    return render(request=request, template_name='menu.html', context={'menu_items': menu, 'admin_menu':is_admin})

def list_dish(request):
    dishes = Dish.objects.all()
    is_admin = check_admin(request)
    return render_to_response(template_name='admin_menu_list.html', context={'dishes':dishes, 'admin_menu':is_admin})

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
    is_admin = check_admin(request)
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
    return render(request=request,template_name='store_dish.html', context={'status':status, 'admin_menu':is_admin, 'category':Dish_category.objects.all()})

def edit_dish(request, id):
    is_admin = check_admin(request)
    status = ''
    try:
        dish = Dish.objects.get(id=id)
    except:
        return HttpResponse("Dish not found!")
    if request.POST:
        name = request.POST['name']
        category = request.POST['category']
        rate = request.POST['rate']
        rate = float(rate)
        available_from = request.POST['available_from']
        available_from = datetime.datetime.strptime(available_from, '%Y-%m-%d').date()
        is_veg = True if 'is_veg' in request.POST else False
        is_available = True if 'is_available' in request.POST else False
        if request.FILES:
            file = request.FILES['file']
            dest_file = settings.BASE_DIR + '/static/images/'+file.name
            with open(dest_file,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        dish.name = name
        dish.category = category
        dish.rate = rate
        dish.available_from = available_from
        dish.isVeg = is_veg
        dish.is_available = is_available
        if request.FILES:
            dish.image = file.name
        dish.save()
        status = 'Dish Saved!'
    return render(request=request, template_name='store_dish.html', context={'dish': dish, 'status':status, 'admin_menu':is_admin, 'category':Dish_category.objects.all()})

def delete_dish(request, id):
    try:
        dish = Dish.objects.get(id=id)
    except:
        return HttpResponse("Dish not found!")
    dish.delete()
    return HttpResponse("Dish removed!")


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        my_admin_user = admin_user.objects.filter(username = username)
        if my_admin_user.count() > 0:
            my_admin_user = my_admin_user[0]
            db_username = my_admin_user.username
            db_password = my_admin_user.password
            if username == db_username and password == db_password:
                response = render(request = request, template_name='login.html', context={'status':'Login Successful!'})
                #notice response usage for cookies
                # response.set_cookie('login_id', '45565$78678#')
                # notice request usage for session
                request.session['login_id'] = '45565$78678#'
            else:
                response = render(request=request, template_name='login.html',
                                  context={'status': 'Login Unsuccessful!'})
        else:
            response = render(request = request, template_name='login.html', context={'status': 'Login Unsuccessful!'})
            # return redirect('/home')
        return redirect('/webpages/home')
    else:
        return render(request = request, template_name='login.html', context={'status':'', 'admin_menu':False})

def logout(request):
    # del request.COOKIES['login_id']
    request.session['login_id'] = None
    return redirect('/webpages/login')

def check_admin(request):
    try:
        # login_id = request.COOKIES['login_id']
        login_id = request.session['login_id']
        if login_id == '45565$78678#':
            return True
        else:
            return False
    except Exception as e:
        return False



# Database interactions
# saving object
# this_order = Order()
# this_order.mobile = mobile
# this_order.order = order
# this_order.save()
#
# # fetching all objects
# orders = Order.objects.all()
#
# # filter - gives multiple objects
# orders = Order.objects.filter(mobile='123434')
# orders = Order.objects.exclude(mobile='123434')
#
# # filter with single object
# order = Order.objects.get(id=1)
#
# # updating single object
# order = Order.objects.get(id=1)
# order.mobile = '1232132'
# order.save()
# Order.objects.get(id=1).update(mobile=1232)
#
# # multiple objects update
# Order.objects.filter(mobile='123434').update(order='ajdflkdlaks')
# orders = Order.objects.filter(mobile='123434')
# for item in orders:
#     item.mobile = 12321
#     item.save()
#     # item.delete()
# Order.objects.filter(mobile='123434').delete()
# Order.objects.get(id=1).delete()
