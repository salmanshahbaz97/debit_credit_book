from django.shortcuts import get_object_or_404, render
from django.http import Http404


from .pagination import DefaultPagination
from .filters import SalesFilter
from .models import Sales
from .serializer import SalesSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class SalesViewSet(ModelViewSet):
        queryset = Sales.objects.all()
        serializer_class = SalesSerializer

        def list(self, request, *args, **kwargs):
            queryset = Sales.objects.all()
            serializer = SalesSerializer(queryset, many=True)
            return Response({'data': serializer.data}, template_name='core/sales_detail.html')


class SalesList(APIView):
    def get(self, request):
        queryset = Sales.objects.all()
        serializer = SalesSerializer(queryset, many=True)
        sum = 0
        for data in serializer.data:
            sum += float(data['amount']) 
        print(sum)
        return render(request, 'core/sales_detail.html', {'records': list(serializer.data), 'total': sum})
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SalesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SalesDetail(APIView):
    """
    Retrieve, update or delete a collection instance.
    """
    def get_object(self, pk):
        try:
            return Sales.objects.get(pk=pk)
        except Sales.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sale = self.get_object(pk)
        serializer = SalesSerializer(sale)
        return Response(serializer.data)

    def put(self, request, pk):
        sale = self.get_object(pk)
        serializer = SalesSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sale = self.get_object(pk)
        sale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
