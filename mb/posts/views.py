from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

    queryset = Post.objects.filter(text__contains='test')  
    #context_object_name = 'all_posts_list' # new

