from django.contrib import admin
from . models import  Clients
from . models import  Products
from . models import  Shopping_Cart
from . models import  Quantity
admin.site.register(Clients)
admin.site.register(Products)
admin.site.register(Shopping_Cart)
admin.site.register(Quantity)
