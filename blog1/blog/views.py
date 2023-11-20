from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post 
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # new
from django.core.paginator import Paginator # new

# Create your views here.
class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    paginate_by = 1  # Set the number of comments per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.post_comments.filter(is_approved=True)
        paginator = Paginator(comments, self.paginate_by)

        page = self.request.GET.get('page')
        comments = paginator.get_page(page)

        context['comments'] = comments
        return context

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    #fields = ['title', 'author', 'body']
    fields = ['title', 'body'] # new
    # fields = '__all__' # all fields except auto id and date 

    def form_valid(self, form): # new
        # set the current user to author
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url=reverse_lazy('home')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

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
