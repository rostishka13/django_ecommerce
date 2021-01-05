from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
class HomeView(ListView):
	model = Post
	template_name = 'blog/home_blog.html'
	#ordering = ['-public_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    reverse_lazy = 'home_blog'