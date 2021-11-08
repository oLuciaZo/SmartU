from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Capacity


# Create your views here.

def index(request):
    capacity = Capacity.objects.all()
    return render(request, 'freespace/index.html', {'capacity':capacity})