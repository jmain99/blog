from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.
from .models import Post

class BlogListView(ListView):
    model= Post
    template_name= 'home.html'

class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields='__all__'

class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']

class BlogDeleteView(DeleteView):
    model= Post
    template_name='post_delete.html'
    success_url= reverse_lazy('home')
