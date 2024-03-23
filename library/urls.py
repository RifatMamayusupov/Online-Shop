from rest_framework import routers
from .views import (CategoryViewSet, 
                    GoodsViewSet, 
                    BuyViewSet, 
                    PaymentViewSet, 
                    OrderStatusViewSet, 
                    GoodsFeaturesViewSet, 
                    CommentViewSet, RateGoodsViewSet)

router = routers.DefaultRouter()
router.register(r'category',CategoryViewSet , basename='category')
router.register(r'goods', GoodsViewSet, basename='goods')
router.register(r'buy', BuyViewSet, basename='buy')
router.register(r'payment',PaymentViewSet , basename='payment')
router.register(r'orderstatus',OrderStatusViewSet,basename='orderstatus')
router.register(r'features',GoodsFeaturesViewSet,basename='features')
router.register(r'comments',CommentViewSet,basename='comments')
router.register(r'rate',RateGoodsViewSet, basename='rate')

urlpatterns = router.urls