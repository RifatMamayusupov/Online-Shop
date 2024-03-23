from django.shortcuts import render
from .serializers import (CategorySerializer,
                          GoodsSerializer,
                          BuySerializer, 
                          PaymentSerializer, 
                          OrderStatusSerializer, 
                          GoodsFeaturesSerializer, 
                          CommentSerializer, RateGoodsSerializer)
from .models import Category, Goods, Payment, GoodsFeatures, Comment, RateGoods, Buy, OrderStatus

# Create your views here.
from rest_framework import mixins, status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from datetime import datetime, timedelta
from rest_framework import generics, permissions

# model and serializers classlar bilan  qo'shilgan viewsetlar

class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
      
      queryset = Category.objects.all()
      serializer_class = CategorySerializer

      def list(self, request):
         queryset = self.get_queryset().filter(self_category=None)
         serializer = CategorySerializer(queryset, many=True)

         return Response(serializer.data)

class GoodsViewSet(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin):
      
      queryset = Goods.objects.all()
      serializer_class = GoodsSerializer
      filter_backends = [filters.OrderingFilter]
      ordering_fields=['price','created_at']
      search_fields=['^model','^name','^model','^type']
      parameters = [
        openapi.Parameter('id', openapi.IN_QUERY, description='izlanishi kerak bo\'lgan ma\'lumot', type=openapi.TYPE_INTEGER),
        openapi.Parameter('name', openapi.IN_QUERY, description='izlanishi kerak bo\'lgan ma\'lumot', type=openapi.TYPE_STRING),
        openapi.Parameter('model', openapi.IN_QUERY, description='izlanishi kerak bo\'lgan ma\'lumot', type=openapi.TYPE_STRING),
        openapi.Parameter('type', openapi.IN_QUERY, description='izlanishi kerak bo\'lgan ma\'lumot', type=openapi.TYPE_STRING),
      ]

      @swagger_auto_schema(manual_parameters=parameters)
      @action(detail=False,methods=['get'])
      def filter_by_fields(self, request):

         object_id = request.query_params.get('id', None)
         name = request.query_params.get('name', None)
         model = request.query_params.get('model', None)
         type = request.query_params.get('type', None)
         queryset=self.queryset

         if object_id:
                 queryset = queryset.filter(id=int(object_id))

         if name:
             queryset = queryset.filter(name__istartswith=name)

         if model:
             queryset = queryset.filter(model__istartswith=model)

         if type:
             queryset=queryset.filter(type__name__istartswith=type)

         serializer = self.get_serializer(queryset, many=True)

         return Response(serializer.data)

class BuyViewSet(viewsets.ModelViewSet):
        
        queryset = Buy.objects.all()
        serializer_class = BuySerializer

class PaymentViewSet(viewsets.ModelViewSet):
          
        queryset = Payment.objects.all()
        serializer_class = PaymentSerializer

class OrderStatusViewSet(viewsets.ReadOnlyModelViewSet):
        
        queryset = OrderStatus.objects.all()
        serializer_class = OrderStatusSerializer

class GoodsFeaturesViewSet(viewsets.ModelViewSet):

       queryset = GoodsFeatures.objects.all()
       serializer_class = GoodsFeaturesSerializer

class CommentViewSet(viewsets.ModelViewSet):

     queryset=Comment.objects.all()
     serializer_class=CommentSerializer
    
     def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

     inputs=openapi.Schema(type=openapi.TYPE_OBJECT,
                          properties={
                              'goods':openapi.Schema(type=openapi.TYPE_STRING),
                              'context':openapi.Schema(type=openapi.TYPE_STRING),
                          })
     @swagger_auto_schema(operation_description='Comment Item',request_body=inputs)
     @action(detail=False,methods=['post'])
     def comment(self,request,*args, **kwargs):
        result=self.queryset.filter(
            goods=request.data['goods'].name,
            comment=request.data['context'],
        )
        
        if Goods.objects.get(item__id=request.data.get('goods')):
            
                request.data['user']=request.user.id
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer) 
        else:
             return Response({'Eror': 'This item temporary is not avaible '})
        return Response(serializer.data)

class RateGoodsViewSet(viewsets.ModelViewSet):
      
      queryset = RateGoods.objects.all()
      serializer_class = RateGoodsSerializer

  


  