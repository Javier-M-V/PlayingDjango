#from rest_framework.views import APIView
#from rest_framework.response import Response
#from django.shortcuts import get_object_or_404

from rest_framework import generics
from .models import Producto, Categoria, SubCategoria
from .serializer import ProductoSerializer, CategoriaSerializer, SubCategoriaSerializer

'''
class ProductoList(APIView):

    def get(self, request):
        prod = Producto.objects.all()[:20]
        data = ProductoSerializer(prod, many=True).data
        return Response(data)


class ProductoDetalle(APIView):
    def get(self, request, pk):
        prod = get_object_or_404(Producto, pk=pk)
        data = ProductoSerializer(prod).data
        return Response(data)

'''


class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetalle(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaSave (generics.CreateAPIView):
    serializer_class = CategoriaSerializer


class SubCategoriaSave (generics.CreateAPIView):
    serializer_class = SubCategoriaSerializer


class CategoriaList (generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class SubcategoriaAllList (generics.ListCreateAPIView):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer


class CategoriaDetall(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class SubcategoriaList(generics.ListCreateAPIView):
    serializer_class = SubCategoriaSerializer

    def get_queryset(self):
        queryset = SubCategoria.objects.filter(categoria_id=self.kwargs["pk"])
        return queryset

