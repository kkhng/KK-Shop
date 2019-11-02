from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# also got Product.objects.filter(), Product.objects.get(), Product.objects.save()
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

