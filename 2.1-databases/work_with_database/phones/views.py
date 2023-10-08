from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorted_by = request.GET.get('sort', 'name')
    sorted_dict = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    template = 'catalog.html'
    context = {'phones': Phone.objects.all().order_by(sorted_dict[sorted_by])}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
