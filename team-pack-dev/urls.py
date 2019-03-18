from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from .views import ReactAppView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('api/', include('scraping.api.urls')),
    path('carstat/', include('carstatistic.api.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^favicon\.ico$', RedirectView.as_view(
        url='/build/favicon.ico', permanent=True)),
    re_path(r'^.*', ReactAppView.as_view()),  # Base URL to load React App
]
