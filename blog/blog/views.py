from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # new
from .models import Post 
from django.urls import reverse_lazy
from .forms import PostForm

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
    # fields = '__all__' # all fields except auto id and date 

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url=reverse_lazy('home')

def blogListFormView(request):
    # creaet instance of the form
    form = PostForm(request.POST)
    # to pass as dictionary form 
    context = {'form':form} 
    return render(request, 'post_new1.html', context)

def blogListHTMLView(request):
    context = {
        'title': request.POST.get('title', None),
        'author': request.POST.get('author', None),
        'body': request.POST.get('body', None),
    }
    return render(request, 'post_new2.html', context)
