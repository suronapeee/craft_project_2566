from django import forms
# mport the User model from django.contrib.auth.models 
# and use it as the queryset for the author field.
from django.contrib.auth.models import User 

class PostForm(forms.Form):
    title = forms.CharField(max_length=200, required=False)
    author = forms.ModelChoiceField(
        queryset=User.objects.all(),  # Use the appropriate queryset for your User model
        #empty_label=None, # This removes the "---------" option in the dropdown
        required=False,
    )
    body = forms.CharField(widget=forms.Textarea, required=False) 