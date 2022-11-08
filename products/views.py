from django.shortcuts import get_object_or_404, render
from .models import Product

# Create your views here.

def products(request):
    pro = Product.objects.all()

    name = None
    desc = None
    pfrom = None
    pto = None
    cs = None

    if'cs' in request.GET:
        cs = request.GET['cs']
        if not cs:
            cs = 'off'

    if 'searchname' in request.GET:
        name =request.GET['searchname']
        if name:
            if cs == 'on':
                pro = pro.filter(name__contains=name)
            else:
                pro = pro.filter(name__icontains=name)
    

    if 'saerchdesc' in request.GET:
        desc =request.GET['saerchdesc']
        if desc:
            if cs == 'on':
                pro = pro.filter(description__contains=desc)
            else:
                pro = pro.filter(description__icontains=desc)


    if 'searchpricefrom' in request.GET and 'serchpriceto' in request.GET:
        pfrom =request.GET['searchpricefrom']
        pto =request.GET['serchpriceto']
        if pfrom and pto:
            if pfrom.isdigit() and pto.isdigit():
                pro = pro.filter(price__gte=pfrom , price__lte=pto)

    context ={
        'products': pro
    }
    return render(request, 'products/products.html', context)

def product(request, pro_id):
    context ={
        'pro':get_object_or_404(Product, pk=pro_id)
    }
    return render(request, 'products/product.html',context )

def search(request):
    return render(request, 'products/search.html')