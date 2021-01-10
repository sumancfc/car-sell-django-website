from django.shortcuts import render
from .models import Car


# Create your views here.
def cars(request):
       all_cars = Car.objects.order_by('-created_date')

       data = {
             'all_cars' : all_cars
       }

       return render(request, 'cars/cars.html', data)

def car_detail(request):
       return render(request, 'cars/car_detail.html')

def search(request):
       return render(request, 'cars/search.html')