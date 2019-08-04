from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Fun & Food")

def contact(request):
    return HttpResponse("This is contact page")