from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import *


# Create your views here.


def render_index(request):
    return render(request, 'ZOO_App/index.html')


def render_animals_list(request):
    return render(request, 'ZOO_App/listagem_animais.html')


def render_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('ZOO_App:index'))
        else:
            return render(request, 'ZOO_App/login.html')
    return render(request, 'ZOO_App/login.html')


def render_register(request):
    if request.method == 'POST':
        if request.POST.get("password") == request.POST.get("password2"):
            if request.POST.get('username').strip() != '' and request.POST.get('email').strip() != '' and request.POST.get('password').strip() != '' and request.POST.get('first_name').strip() != '' and request.POST.get('last_name').strip() != '' and request.POST.get('address').strip() != '' and request.POST.get('TIN').strip() != '':
                user = User.objects.create_user(request.POST.get("username"), request.POST.get("email"), request.POST.get("password"))
                user.first_name = request.POST.get("first_name")
                user.last_name = request.POST.get("last_name")
                user.save()
                utilizador = Utilizador(user=user, data_nascimento=request.POST.get("birth_date"), morada=request.POST.get("address"), numero_contribuinte=request.POST.get("TIN"))
                utilizador.save()
                user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
                login(request, user)
                return HttpResponseRedirect(reverse('ZOO_App:index'))
            else:
                return render(request, 'ZOO_App/registar.html', {'error_message_empty_fields': "Não pode haver campos vazios!"})
        else:
            return render(request, 'ZOO_App/registar.html', {'error_message_password': "Passwords não são iguais!"})
    else:
        return render(request, 'ZOO_App/registar.html')


@login_required(login_url='/votacao')
def render_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('ZOO_App:login'))

def render_about(request):
    list = getProductsInCart(request)
    return render(request, 'ZOO_App/about.html', {'all' :list})


def render_noticias(request):
    lista_noticias_total = Noticia.objects.all()
    lista_noticias_user = UtilizadorNoticia_pk.objects.filter(utilizador=request.user.utilizador)
    lista_tags = {}
    lista_noticias = []
    lista_noticias_recomendadas = []
    listCart = getProductsInCart(request)
    for item in lista_noticias_user:
        noticia = item.noticia
        lista_noticias = lista_noticias + [noticia]
        lista_tags_noticia = NoticiaTag_pk.objects.filter(noticia=noticia)
        for item2 in lista_tags_noticia:
            if lista_tags is not None:
                if item2.tag.nome in lista_tags:
                    lista_tags[item2.tag.nome] = lista_tags[item2.tag.nome] + 1
                else:
                    lista_tags[item2.tag.nome] = 1
            else:
                lista_tags[item2.tag.nome] = 1
    for item in NoticiaTag_pk.objects.all():
        if item.noticia not in lista_noticias and item.tag not in lista_tags.keys():
            lista_noticias_recomendadas = lista_noticias_recomendadas + [item.noticia]
    lista_noticias_recomendadas = lista_noticias_recomendadas + list(lista_noticias_total)
    lista_noticias_recomendadas = lista_noticias_recomendadas[0:4]
    lista_noticias_total = list(lista_noticias_total)
    if "searchTerm" in request.POST:
        searchTerm = request.POST["searchTerm"]
        for item in lista_noticias_total.copy():
            if item.descricao.find(searchTerm) == -1 and item.titulo.find(searchTerm) == -1:
                lista_noticias_total.remove(item)
        for item in lista_noticias_recomendadas.copy():
            if item.descricao.find(searchTerm) == -1 and item.titulo.find(searchTerm) == -1:
                lista_noticias_recomendadas.remove(item)
    return render(request, 'ZOO_App/listagem_noticias.html', {'noticias': lista_noticias_total,'recomendadas': lista_noticias_recomendadas[0:4], 'all' :listCart})


def render_detalhe_noticia(request):
    return
def render_precario(request):
    bilhetes = Bilhete.objects.all()
    list = getProductsInCart(request)
    return render(request, 'ZOO_App/precario.html', {'all' :list})

def render_shop(request):
    product_list = Produto.objects.all()
    list = getProductsInCart(request)
    product_types=  []
    for product in product_list:
        if product.categoria not in product_types:
            product_types.append(product.categoria)

    context = {'product_list': product_list,'all' :list, "product_types": product_types
    }
    return render(request, 'ZOO_App/shop_archive.html', context)

def render_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    list = getProductsInCart(request)
    return render(request, 'ZOO_App/product_info.html', {'produto': produto,'all' :list})

#@login_required(login_url='/login')
def addProductToCart(request):
    if request.method == 'POST':
        try:
            produto_id = request.POST.get("produto_id")
            quantidade = request.POST.get("quantidade")
        except KeyError:
            return render(request, 'ZOO_App/shop.html')
        #request.user.id
        if produto_id:
            produto = get_object_or_404(Produto, pk=produto_id)
            utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
            try:
                pcc_pk = ProdutoCarinhoCompras_pk.objects.get(produto=produto, utilizador=utilizador)
            except ProdutoCarinhoCompras_pk.DoesNotExist:
                pcc_pk2 = ProdutoCarinhoCompras_pk(produto=produto, utilizador=utilizador, quantidade = quantidade)
                pcc_pk2.save()
                return HttpResponseRedirect(reverse('ZOO_App:shop'))
            #pcc_pk = get_object_or_404(ProdutoCarinhoCompras_pk, pk=questao_id)
            pcc_pk.quantidade+=int('0' + quantidade)
            pcc_pk.save()
            return HttpResponseRedirect(reverse('ZOO_App:shop'))
        else:
            print("Produto selecionado não existe")
    else:
        return render(request, 'ZOO_App/shop.html')  


def auxGetProductsInCart(utilizador):
    pcc_pk = ProdutoCarinhoCompras_pk.objects.filter(utilizador=utilizador)
    list=[]
    for item in pcc_pk:
        list.append(item)
    return list  

def getProductsInCart(request):
    product_list = Produto.objects.all()
    utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
    list = auxGetProductsInCart(utilizador)
    
#    pcc_pk = ProdutoCarinhoCompras_pk.objects.filter(utilizador=utilizador)
#    dict={}
#    for item in pcc_pk:
#        dict[item]=ProdutoCarinhoCompras.objects.get(produtocarinhocompras_pk=item)
        #list.append(ProdutoCarinhoCompras.objects.filter(produtocarinhocompras_pk=item))
    
    #pcc1 = ProdutoCarinhoCompras.objects.filter(produtocarinhocompras_pk=pcc_pk)

    #return render(request, 'ZOO_App/shop_archive.html', {'pcc_pk':pcc_pk, 'pcc': list, 'product_list': product_list})
    #return HttpResponse("{% for key, value in " + dict + ".items %}")
    return list
    #return render(request, 'ZOO_App/shop_archive.html', {'all':dict, 'product_list': product_list})

def render_purchase(request):
    #utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
    #dict = auxGetProductsInCart(utilizador)
    list = getProductsInCart(request)
    return render(request, 'ZOO_App/purchase.html', {'all':list})

def finishPurchase(request):
    utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
    list = auxGetProductsInCart(utilizador)
    current_datetime = timezone.now()  
    precototal = getTotalPrice(list)
    fatura = Fatura(data=current_datetime, preco_total=float(precototal), utilizador=utilizador)
    fatura.save()
    for item in list:
        faturaprodutopk = FaturaProduto_pk(fatura= fatura, produto=item.produto, quantidade=item.quantidade)
        faturaprodutopk.save()
    emptyCart(request)    
    return render(request, 'ZOO_App/about.html', {'all':list}) 

    

def getTotalPrice(list):
    sum=0
    for item in list:
        sum += item.produto.preco * item.quantidade
    return sum    

def emptyCart(request):
    product_list = Produto.objects.all()
    utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
    list = auxGetProductsInCart(utilizador) 
    for item in list:
        item.delete()
    return render(request, 'ZOO_App/shop_archive.html', {'product_list': product_list}) 
    
def deleteProductFromCart(request, produto_id):
    utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
    produto = get_object_or_404(Produto, pk=produto_id)
    list = auxGetProductsInCart(utilizador) 
    for item in list:
        if item.produto == produto:
            item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    #return getProductsInCart(request)   
def takeProductFromCart(request, produto_id):
    utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
    produto = get_object_or_404(Produto, pk=produto_id)
    list = auxGetProductsInCart(utilizador) 
    for item in list:
        if item.produto == produto:
            item.quantidade -=1
            item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def sumProductToCart(request, produto_id):
    utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
    produto = get_object_or_404(Produto, pk=produto_id)
    list = auxGetProductsInCart(utilizador) 
    for item in list:
        if item.produto == produto:
            item.quantidade +=1
            item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))     
            
def render_minhascompras(request):
    list = getProductsInCart(request)
    utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
    faturas = Fatura.objects.filter(utilizador=utilizador)
    dict={}
    print(faturas[0].data)
    for item in faturas:
        dict[item]=FaturaProduto_pk.objects.filter(fatura=item)  
    return render(request, 'ZOO_App/minhascompras.html', {'all' :list, 'fatura':dict})

def addComentario(request, noticia_id):
    if request.method == 'POST':
        try:
            comentario = request.POST.get("comment")
        except KeyError:
            return render(request, 'ZOO_App/about.html')
    utilizador = get_object_or_404(Utilizador, user_id=request.user.id)
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    current_datetime = timezone.now() 
    #comentario=""
    #list = auxGetProductsInCart(utilizador) 
    noticia_utilizador = UtilizadorNoticia_pk.objects.get(utilizador=utilizador, noticia=noticia)
    utilizador_comentario = UtilizadorComentario(UtilizadorNoticia_pk=noticia_utilizador, data=current_datetime, comentario=comentario)
    utilizador_comentario.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))   
    
