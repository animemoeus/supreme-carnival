"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.api.urls", namespace="accounts-api")),
    path("api/countries/", include("countries.api.urls", namespace="countries-api")),
    path("api/categories/", include("categories.api.urls", namespace="categories-api")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("countries/", include("countries.urls", namespace="countries")),
    path("categories/", include("categories.urls", namespace="categories")),
]
