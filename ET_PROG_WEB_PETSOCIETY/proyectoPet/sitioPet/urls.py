from django.urls import path
from .views import cart,store,checkout,updateItem,processOrder,form_boleta, form_del_bole, form_del_cli, form_del_prod, form_mod_boleta, form_mod_prod, index, index1, indexapi, indeximc, indexpruebahtmlcontacto, logIn, form_producto,mostrardatos,form_cliente,form_mod_cli, registerpets, somos4


urlpatterns = [
    path('', index, name="index"),
    path('somos4/', somos4, name="somos4"),
    path('indexapi/', indexapi, name="indexapi"),
    path('indexpruebahtmlcontacto/', indexpruebahtmlcontacto, name="indexpruebahtmlcontacto"),
    path('registerpets/', registerpets, name="registerpets"),
    path('indeximc/', indeximc, name="index-imc"),
    path('index1/', index1, name="index1"),
    path('mostrardatos/',mostrardatos,name="mostrardatos"),
    path('form_producto/',form_producto,name="form_producto"),
    path('form_mod_prod/<id>',form_mod_prod,name="form_mod_prod"),
    path('form_del_prod/<id>',form_del_prod,name="form_del_prod"),
    path('form_boleta/',form_boleta,name="form_boleta"),
    path('form_mod_boleta/<id>',form_mod_boleta,name="form_mod_boletae"),
    path('form_del_bole/<id>',form_del_bole,name="form_del_bole"),
    path('form_cliente/',form_cliente,name="form_cliente"),
    path('form_mod_cli/<id>',form_mod_cli,name="form_mod_cli"),
    path('form_del_cli/<id>',form_del_cli,name="form_del_cli"),
    path('iniciosesion/',logIn,name="login"),
    path('store', store, name="store"),
	path('cart/', cart, name="cart"),
	path('checkout/', checkout, name="checkout"),
	path('update_item/', updateItem, name="update_item"),
	path('process_order/', processOrder, name="process_order"),
]