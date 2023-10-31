
from django.shortcuts import render
from django.core.paginator import Paginator
from shop.models import Product

# Create your views here.
def index(request):
    product_object = Product.objects.all()
    #nous voulons faire un champs de rechercher
    item_name = request.GET.get('item-name')
    item_price = request.GET.get('item-price')
    if ((item_name != '' or item_price !='') and (item_name is not None or item_price is not None)):
        product_object = Product.objects.filter(title__icontains=item_name)
        product_object = product_object.filter(price__icontains=item_price)
    #__icontains est l'équivalent de %like% en sql

    #faisons donc la pagination
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})

def show(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/show.html', {'product': product_object})