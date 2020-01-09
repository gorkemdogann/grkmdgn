from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Post

class BlogPageView(ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 3

class BlogDetailView(DetailView):
    model = Post
    template_name = "post.html"


