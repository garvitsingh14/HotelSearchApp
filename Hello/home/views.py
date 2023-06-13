from django.shortcuts import render,HttpResponse
from home.models import ContactTable
# from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    # context = {
    #     "variable" : "garvit"
    # }
    return render(request,'index.html')

def service(request):
    return render(request,'service.html')

def about(request):
    return render(request,'about.html')

def details(request):
    return render(request,'details.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
                
        contact = ContactTable(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, "Profile details updated sucessfully !")
        
    return render(request,'contact.html')