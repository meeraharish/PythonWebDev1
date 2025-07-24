from django.contrib import admin
from . models import Product
from . models import Offer

class ProductAdmin(admin.ModelAdmin): #Model admin controls admin interface behaviour ex: ordering etc
    list_display=('name','price','stock') # tells which columns should be visible 

class OfferAdmin(admin.ModelAdmin):
    list_display=('code','discount')


admin.site.register(Product,ProductAdmin) # we want to manage the products that we develop on the admin page
admin.site.register(Offer,OfferAdmin)