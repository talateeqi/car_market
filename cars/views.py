from django.shortcuts import render
from .models import Car

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	#Complete Me
	return render(...)


def car_update(request, car_id):
	#Complete Me
	return render(...)


def car_delete(request, car_id):
	#Complete Me
	return render(...)