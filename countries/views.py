from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView

from .forms import AddCountryForm, EditCountryForm
from .models import Country


class CountryView(View):
    def get(self, request):
        countries = Country.objects.all().order_by("-id")

        context = {"countries": countries}

        return render(self.request, "countries/index.html", context)


class AddCountryView(View):
    def get(self, request):
        return render(self.request, "countries/add.html", {"form": AddCountryForm})

    def post(self, request):
        form = AddCountryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("countries:index")

        return render(self.request, "countries/add.html", {"form": form})


class EditCountryView(UpdateView):
    model = Country
    form_class = EditCountryForm
    template_name = "countries/edit.html"
    success_url = reverse_lazy("countries:index")


class DeleteCountryView(DeleteView):
    model = Country
    template_name = "countries/delete.html"
    success_url = reverse_lazy("countries:index")
