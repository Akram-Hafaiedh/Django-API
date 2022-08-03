from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewset

router = DefaultRouter()
router.register('product-abc', ProductViewset, basename='products')

print(router.urls)
urlpatterns = router.urls