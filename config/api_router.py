from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from study_shop.users.api.views import UserViewSet
from study_shop.core.api.views import ClothesViewSet, CategoryViewSet, SuppliersViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('users', UserViewSet)
router.register('clothes', ClothesViewSet)
router.register('category', CategoryViewSet)
router.register('suppliers', SuppliersViewSet)



app_name = "api"
urlpatterns = router.urls
