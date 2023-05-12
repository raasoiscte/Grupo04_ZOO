from django.urls import path
from . import views

app_name = 'ZOO_App'
urlpatterns = [
    path('', views.render_index, name='index'),
    path('animais', views.render_animals_list, name='listagem_animais'),
    path('login', views.render_login, name='login'),
    path('registar', views.render_register, name='registar'),
    path('logout', views.render_logout, name='logout'),
    path('about',views.render_about, name='about'),
    path('noticias',views.render_noticias, name='listagem_noticias'),
    path('noticia/<int:noticia_id>',views.render_detalhe_noticia, name='detalhe_noticia'),
    path('shop',views.render_shop, name='shop'),
    path('<int:produto_id>',views.render_produto, name='produto'),
    path('addProductToCart',views.addProductToCart, name='addProductToCart'),
    path('getProductsInCart',views.getProductsInCart, name='getProductsInCart'),
    path('precario',views.render_precario, name='precario'),
    path('informacao_pessoal',views.render_informacao_pessoal, name='informacao_pessoal'),
path('alterar_password',views.render_alterar_password, name='alterar_password'),
]