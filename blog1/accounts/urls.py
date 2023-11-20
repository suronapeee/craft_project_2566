from django.urls import path
from .views import SignUpView, ChangeView 
from .views import register # new

urlpatterns = [
  path('signup/', SignUpView.as_view(), name='signup'),
  #path('signup/', register, name='signup'), # new
  path('change_user/<int:pk>/', ChangeView.as_view(), name='change_user'), 
]
