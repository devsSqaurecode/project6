from django.shortcuts import render, get_object_or_404
from .models import Product, Company
from .filters import ProductFilter
# Create your views here.

def home(request):
    products = Product.objects.all()
    companies  = Company.objects.all()
    productFilter = ProductFilter(request.GET, queryset=products)
    context = {
        'products':products,
        'productFilter':productFilter
    }
    return render(request, 'grocery/index.html',context)


def detail(request,prod_id):
    context = {
        'data': get_object_or_404(Product, pk=prod_id)
    }
    return render(request,'grocery/detail.html',context)

    