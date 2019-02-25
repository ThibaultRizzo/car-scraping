from scraping.api.views import CarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CarViewSet, base_name='cars')
urlpatterns = router.urls
