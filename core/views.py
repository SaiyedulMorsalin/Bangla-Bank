from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class HOMEVIEW(TemplateView):
    template_name = "index.html"
