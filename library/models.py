from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    self_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Goods(models.Model):

    name = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    # image = models.ImageField(upload_to='goods_image')
    price = models.IntegerField()
    model = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return  self.name

class Buy(models.Model):

     user = models.ForeignKey(User, on_delete=models.CASCADE)
     goodsid = models.ForeignKey(Goods,on_delete=models.SET_NULL,null=True, related_name='buyid')
     phone_number = models.CharField(max_length=20)
     region = models.CharField(max_length=50)

     def __str__(self):
        return self.region

class Payment(models.Model):
     
     id_card = models.CharField(max_length=30)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.id_card

class OrderStatus(models.Model):

     order_num = models.IntegerField(null=True, blank=True)
     order_phone_number = models.CharField(max_length=16)

     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return str(self.order_num) 
        
class GoodsFeatures(models.Model):

    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    screan = models.CharField(max_length=20)
    operation_system = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.goods 
        
class Comment(models.Model):

    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.content[:20]

class RateGoods(models.Model):
     
     goods = models.ManyToManyField(to=Goods)
     rate = models.IntegerField()

     def __str__(self):
        return self.goods.name
