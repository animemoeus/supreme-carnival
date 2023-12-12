from django.urls import path

from .views import CategoryListView, CreateCategoryView

urlpatterns = [
    path("", CategoryListView.as_view(), name="index"),
    path("create/", CreateCategoryView.as_view(), name="create"),
]

app_name = "categories"
