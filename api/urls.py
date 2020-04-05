from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .apiviews import ProductoDetalle, ProductoList, CategoriaList, \
    SubcategoriaList, CategoriaDetall, SubcategoriaAllList, SubcategoriaAdd, \
    ProductoViewSet, UserCreate, Login

from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register('v2/productos', ProductoViewSet, basename='productos')
urlpatterns = [

    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),
    path('v1/categorias/',  CategoriaList.as_view(), name='categoria_save'),
    path('v1/subcategorias/', SubcategoriaAllList.as_view(), name='subcategoria_save'),
    path('v1/categorias/<int:pk>',  CategoriaDetall.as_view(), name='categoria_detalle'),
    path('v1/categorias/<int:pk>/subcategorias', SubcategoriaList.as_view(), name='sc_list'),
    path('v1/categorias/<int:cat_pk>/addsubcategorias', SubcategoriaAdd.as_view(), name='cat_add'),
    path('v3/usuarios/', UserCreate.as_view(), name='create_user'),
    path('v3/login/', Login.as_view(), name='login'),
    path('v3/login-drf/', views.obtain_auth_token, name='logindrf'),
]
urlpatterns += router.urls
'''  "username": "Javieralf",
    "email": "javier.moreno.vilaplana@gmail.com",
    "password": "123456."'''