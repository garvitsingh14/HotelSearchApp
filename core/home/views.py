from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    peoples = [
        {'name' : 'Garvit Singh', 'age': 24},
        {'name' : 'Harsh Sharma', 'age': 21},
        {'name' : 'Garv Gupta', 'age': 23},
        {'name' : 'Vansh Aggarwal', 'age': 22},
        {'name' : 'Isha Khurana', 'age': 14}
    ]
    
    vegetables = ['Pumpkin','Tomato','Apple']
        
    return render(request,"index.html", context = {'peoples':peoples,'vegetables':vegetables})

def about(request):
    context = {'page':'About'}
    return render(request,"about.html",context)

def contact(request):
    context = {'page':'Contact'}
    return render(request,"contact.html",context)