from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy # new
from .forms import CustomUserCreationForm, CustomUserChangeForm # new
from .models import CustomUser # new
# Create your views here.

class SignUpView(CreateView):
  #form_class = UserCreationForm
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})    

class ChangeView(UpdateView):
  model = CustomUser
  form_class = CustomUserChangeForm
  success_url = reverse_lazy('login')
  template_name = 'registration/change.html'


