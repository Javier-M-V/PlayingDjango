from django.urls import path
from .apiviews import ProductoDetalle, ProductoList, CategoriaList, \
    SubcategoriaList, CategoriaDetall, SubcategoriaAllList

urlpatterns = [

    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),
    path('v1/categorias/',  CategoriaList.as_view(), name='categoria_save'),
    path('v1/subcategorias/', SubcategoriaAllList.as_view(), name='subcategoria_save'),
    path('v1/categorias/<int:pk>',  CategoriaDetall.as_view(), name='categoria_detalle'),
    path('v1/categorias/<int:pk>/subcategorias', SubcategoriaList.as_view(), name='sc_list'),

]
