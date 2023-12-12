from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import CreateCountryForm, EditCountryForm
from .models import Country


class CountryListView(ListView):
    model = Country
    queryset = Country.objects.all().order_by("-id")
    paginate_by = 10
    template_name = "countries/index.html"


class CreateCountryView(CreateView):
    model = Country
    form_class = CreateCountryForm
    template_name = "countries/create.html"
    success_url = reverse_lazy("countries:index")


class EditCountryView(UpdateView):
    model = Country
    form_class = EditCountryForm
    template_name = "countries/edit.html"
    success_url = reverse_lazy("countries:index")


class DeleteCountryView(DeleteView):
    model = Country
    template_name = "countries/delete.html"
    success_url = reverse_lazy("countries:index")
