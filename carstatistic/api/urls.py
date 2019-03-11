from carstatistic.api import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('numbers/', views.get_highlighted_number),
    path('treemaps/', views.get_vendor_treemaps),
    path('boxplot/', views.get_boxplot),
]

urlpatterns = format_suffix_patterns(urlpatterns)
