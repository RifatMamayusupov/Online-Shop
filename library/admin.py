from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'created_at']

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name','describtion', 'price', 'model','position']

    def describtion(self, obj):
        return obj.detail[:20]

@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):

    list_display = ['name','goodsid','phone_number','region']

    def name(self, obj):
        return obj.user

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = ['id_card','created_at']

@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):

    list_display =['order_num','order_phone_number', 'created_at']

@admin.register(GoodsFeatures)
class GoodsFeaturesAdmin(admin.ModelAdmin):
    list_display = ['goods','size','color','screan','operation_system', 'created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['name', 'goods', 'context','created_at']

    def name(self, obj):
        return obj.auther
    
    def goods(self, obj):
        return obj.goods.name

    def context(self, obj):
        return obj.content[:20]

@admin.register(RateGoods)
class RateGoodsAdmin(admin.ModelAdmin):
    list_display = ['item','rate']

    def item(self, obj):
        return obj.goods.name

