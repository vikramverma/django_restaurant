from django.shortcuts import render, HttpResponse, render_to_response

# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')

def contact(request):
    phone_no = "0120-1234567"
    return render(request=request, template_name='contact-us.html', context={'phone_no':phone_no})