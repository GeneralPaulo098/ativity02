from django.shortcuts import render,redirect
from . models import Products
from . forms import ProductsForm
import json

def home(request):
    soma = request.session.get('soma', 1001)
    request.session['soma'] = soma + 1
    return render(request,'home.html')

def products_list(request):
    if(request.method=='POST'):
        pesquisa = request.POST.get('pesquisa')
        if (pesquisa == 'cres'):      
            products = Products.objects.order_by('name')
            return render(request,'products/list.html',{'products':products})

        elif (pesquisa == 'decres'):
            products = Products.objects.order_by('-name')
            return render(request,'products/list.html',{'products':products})
        elif (pesquisa == 'maior'):
            products = Products.objects.order_by('-value')
            return render(request,'products/list.html',{'products':products})
            
        elif (pesquisa == 'menor'):
            products = Products.objects.order_by('value')
            return render(request,'products/list.html',{'products':products})
    else:
        products = Products.objects.all()
        return render(request,'products/list.html',{'products':products})
    
def save_card(request,id):
    product = Products.objects.get(pk=id)
    list_card = request.session.get('card',[])
    list_card.append(product.id)
    request.session['card']= list_card
    return redirect('/ativity/product/')

def products_show(request,id):
    product = Products.objects.get(pk=id)
    return render(request, 'products/show.html',{'product':product})

def product_create(request):
    if(request.method=='POST'):
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ativity/product/')
        else:
            return render(request,'products/form.html',{'form':form})     
    else:
        form = ProductsForm()
        return render(request,'products/form.html',{'form':form})

