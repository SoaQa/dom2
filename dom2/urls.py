"""dom2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from dom2.settings import SITE_URL_PREFIX
from news.views import NewsViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet, basename='Novelty')

urlpatterns = [
    path(SITE_URL_PREFIX + 'admin/', admin.site.urls),
    path(SITE_URL_PREFIX + 'api-auth/', include('rest_framework.urls')),
    path(SITE_URL_PREFIX + 'media/', include('media.urls')),
    path(SITE_URL_PREFIX, include(router.urls))
]
print(router.urls)