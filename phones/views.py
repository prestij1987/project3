from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.getlist('sort')
    if sort:
        if sort[0] == 'name':
            phones = Phone.objects.order_by('name')
        if sort[0] == 'min_price':
            phones = Phone.objects.order_by('price')
        if sort[0] == 'max_price':
            phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug=slug)
    template = 'product.html'
    context = {}
    return render(request, template, context)
