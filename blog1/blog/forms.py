from django import forms
# import the User model from django.contrib.auth.models 
# and use it as the queryset for the author field.
#from django.contrib.auth.models import User 
from accounts.models import CustomUser  # Import your CustomUser model

class PostForm(forms.Form):
    title = forms.CharField(max_length=200, required=False)
    author = forms.ModelChoiceField(
        # Use the appropriate queryset for your User model
        #queryset=User.objects.all(),
        queryset=CustomUser.objects.all(),  
        #empty_label=None, # removes the "---" option in the dropdown
        required=False,
    )
    body = forms.CharField(widget=forms.Textarea, required=False) 

