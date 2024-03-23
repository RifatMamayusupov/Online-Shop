from rest_framework import serializers
from .models import Category, Goods, Buy, Payment, OrderStatus, GoodsFeatures, Comment, RateGoods
import json


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'children', 'created_at']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['children'] = self.get_children(instance)
        return response
    
    def get_children(self, instance):
        children = Category.objects.filter(self_category=instance)
        return CategorySerializer(children, many=True).data

class GoodsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Goods
        fields = '__all__'

class BuySerializer(serializers.ModelSerializer):

    class Meta:
        model = Buy
        fields = "__all__"
    
    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['auther'] = instance.user.username
        response['item'] = instance.goodsid.name
        response['phone'] = instance.phone_number
        response['region'] = instance.region
        del response['phone_number']
        del response['user']
        del response['goodsid']
        
        return response

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class GoodsFeaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsFeatures
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['item']=instance.goods.name
        del response['goods']
        return response


class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['auther'] = instance.user.username
        response['goods'] = GoodsSerializer(Goods.objects.get(id=response["goods"]), many=False).data
        return response

class RateGoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RateGoods
        fields = "__all__"
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['item'] = instance.goods.first().name
        del response['goods']
        return  response
