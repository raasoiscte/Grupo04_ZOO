from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ZOO_App'
urlpatterns = [
    path('', views.render_index, name='index'),
    path('login', views.render_login, name='login'),
    path('registar', views.render_register, name='registar'),
    path('logout', views.render_logout, name='logout'),
    path('about',views.render_about, name='about'),
    path('noticias',views.render_noticias, name='listagem_noticias'),
    path('noticia/<int:noticia_id>',views.render_detalhe_noticia, name='detalhe_noticia'),
    path('shop',views.render_shop, name='shop'),
    path('<int:produto_id>/render_produto',views.render_produto, name='produto'),
    path('addProductToCart',views.addProductToCart, name='addProductToCart'),
    path('getProductsInCart',views.getProductsInCart, name='getProductsInCart'),
    path('purchase',views.render_purchase, name='purchase'),
    path('finishPurchase',views.finishPurchase, name='finishPurchase'),
    path('emptyCart',views.emptyCart, name='emptyCart'),
    path('<int:produto_id>/deleteProductFromCart',views.deleteProductFromCart, name='deleteProductFromCart'),
    path('<int:produto_id>/takeProductFromCart',views.takeProductFromCart, name='takeProductFromCart'),
    path('<int:produto_id>/sumProductToCart',views.sumProductToCart, name='sumProductToCart'),
    path('precario',views.render_precario, name='precario'),
    path('informacao_pessoal',views.render_informacao_pessoal, name='informacao_pessoal'),
    path('alterar_password',views.render_alterar_password, name='alterar_password'),
    path('minhascompras',views.render_minhascompras, name='minhascompras'),
    path('addComentario/<int:noticia_id>',views.addComentario, name='addComentario'),
    path('bilheteCompra/<int:crianca>/<int:adulto>/<int:senior>', views.bilheteCompra, name='bilheteCompra'),
    path('noticia/<int:noticia_id>/adicionar_like', views.render_adicionar_like, name='adicionar_like'),
    path('noticia/<int:noticia_id>/remover_like', views.render_remover_like, name='remover_like'),
    path('createProduct',views.render_createProduct, name='createProduct'),
    path('deleteProduct/<int:produto_id>',views.render_deleteProduct, name='deleteProduct'),
    path('noticias/criarNoticia',views.render_criar_noticia, name='criar_noticia'),
    path('noticia/<int:noticia_id>/remover_noticia',views.render_remover_noticia, name='remover_noticia'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)