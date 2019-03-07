from django.contrib import admin
from django.urls import path, include, re_path
# from django.views.generic import TemplateView
from articles.views import ReactAppView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('articles.api.urls')),
    path('car-api/', include('scraping.api.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^.*', ReactAppView.as_view()),  # Base URL to load React App
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
