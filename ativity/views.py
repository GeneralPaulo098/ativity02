from django.shortcuts import render,redirect
from . models import Products
from . forms import ProductsForm
from . models import Shopping_Cart
from . models import Clients
from . models import Quantity
from datetime import date


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
   

def cart(request):
    e = request.session['card']
    c = []
    soma = 0
    for i in e:
        product = Products.objects.get(pk=i)
        c.append(product)
        soma = soma + product.value
        
    return render(request,'products/cart.html',{'c':c, 'soma':soma})

def final(request):
    e = request.session['card']
    q = []
    cliente = Clients.objects.get(pk=1)
    data_atual = date.today()
    card = Shopping_Cart.objects.create(client=cliente,date=data_atual)
    Shopping_Cart.save(card)
    for i in e:
        product = Products.objects.get(pk=i)
        quan = Quantity.objects.create(quantity=1,product=product,card=card)


    
    del request.session['card']

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

