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
    success_url = reverse_lazy('home_blog')


class DeletePostView(DeleteView):
	model = Post
	template_name = 'blog/delete_post.html'
	success_url = reverse_lazy('home_blog')

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'blog/update_post.html'
	success_url = reverse_lazy('home_blog')


class AddCommentView(CreateView):
	model = Post
	form_class = CommentForm
	template_name = 'blog/add_comment.html'
	success_url = reverse_lazy('home_blog')

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)


	# def form_valid(self, form):
	# 	form.instance.post_id = self.kwargs['pk']
 #    	return super().form_valid(form)

