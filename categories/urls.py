from django.urls import path

from .views import (
    CategoryListView,
    CreateCategoryView,
    DeleteCategoryView,
    UpdateCategoryView,
)

urlpatterns = [
    path("", CategoryListView.as_view(), name="index"),
    path("create/", CreateCategoryView.as_view(), name="create"),
    path("<int:pk>/delete/", DeleteCategoryView.as_view(), name="delete"),
    path("<int:pk>/update/", UpdateCategoryView.as_view(), name="update"),
]

app_name = "categories"
