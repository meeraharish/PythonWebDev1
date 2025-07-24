from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Product


#WHEN IN URL: /Product then request must come to index method 
def index(request):
    product=Product.objects.all() #Fetches all products from the database.
    #return HttpResponse('Hello World')
    return render(request, 'products/index.html',{'products':product})
    #return HttpResponse("It works!")

def new(request):
    return HttpResponse('new products')

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('index')


def cart_view(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    
    cart_items = []
    total = 0
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total': total})