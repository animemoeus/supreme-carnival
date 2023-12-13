from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import CreateCategoryForm, UpdateCategoryForm
from .models import Category


class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all().order_by("-id")
    paginate_by = 10
    template_name = "categories/index.html"


class UpdateCategoryView(UpdateView):
    model = Category
    form_class = UpdateCategoryForm
    template_name = "categories/update.html"
    success_url = reverse_lazy("categories:index")


class CreateCategoryView(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = "categories/create.html"
    success_url = reverse_lazy("categories:index")


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = "categories/delete.html"
    success_url = reverse_lazy("categories:index")
