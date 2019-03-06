from scraping.api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'cars', views.CarViewSet, base_name='cars')
# urlpatterns = router.urls


urlpatterns = [
    path('scrap/', views.scrap_websites),
    path('vendors/', views.getVendorTreemap),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
