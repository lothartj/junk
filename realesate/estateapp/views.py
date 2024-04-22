from django.shortcuts import render, redirect
from .models import Register
from django.http import HttpResponse
import time

def time3():
    time.sleep(2)
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        surname = request.POST.get('Surname')
        age = request.POST.get('Age')

        new_register = Register(Name=name, Surname=surname, Age=age)
        new_register.save()

        register = Register.objects.all()

        return redirect('success', {'register':register} )
    
    return render(request, 'index.html' )

def success(request):
    return render(request, 'success.html')