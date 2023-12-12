from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CreateCountryForm, EditCountryForm
from .models import Country


class CountryView(View):
    def get(self, request):
        countries = Country.objects.all().order_by("-id")

        context = {"countries": countries}

        return render(self.request, "countries/index.html", context)


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
