from django.urls import path
from . import views # . is current directory 

#/product
#/product/new
#/product/trending 
# we are taking '' as the url without the /product
urlpatterns=[
    path('',views.index,name='index'),
    path('new',views.new),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart')
] # here , we are passing a reference to the index function in the view module(view.py)
#django will take care of executing the index function 
 