from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Country


class CountryView(View):
    def get(self, request):
        countries = Country.objects.all()

        context = {"countries": countries}

        return render(self.request, "countries/index.html", context)
