from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import *    
# Create your views here.

class Home(ListView):
    model = Post
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Contact(CreateView):
    model = Murojaat
    template_name = "contact.html"
    fields = "__all__"
    

class Reklama(TemplateView):
    template_name = "reklama.html"

class Team(TemplateView):
    template_name = "team.html"

class  ArticleDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
