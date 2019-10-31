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
    list_cart = request.session.get('cart',[])
    flag = False
    for i in list_cart:
        if product.id == int(i['id']):
            dados = {
                'id':product.id,
                'quantidade':i['quantidade']+1
                }
            list_cart.remove(i)
            list_cart.append(dados)
            flag = True     
    if flag == False:
        dados={
            'id':product.id,
            'quantidade':1
        }
        list_cart.append(dados)

    print(list_cart)
    request.session['cart']= list_cart
    return redirect('/ativity/product/')
   

def cart(request):
    e = request.session['cart']
    soma = 0
    c = []
    for i in e:
        product = Products.objects.get(pk= int(i['id']))
        v = product.value * int(i['quantidade'])
        soma = soma + v
        dados = {
            'name': product.name,
            'value': product.value,
            'value_t': v,
            'quantidade':i['quantidade']
        }
        c.append(dados)
        
    return render(request,'products/cart.html',{'c':c, 'soma':soma})

def final(request):
    e = request.session['cart']
    cliente = Clients.objects.get(pk=1)
    data_atual = date.today()
    cart = Shopping_Cart.objects.create(client=cliente,date=data_atual)
    Shopping_Cart.save(cart)
    for i in e:
        product = Products.objects.get(pk=int(i['id']))
        quan = Quantity.objects.create(quantity=int(i['quantidade']),product=product,cart=cart)

    del request.session['cart']
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

