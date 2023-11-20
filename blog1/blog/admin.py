from django.contrib import admin
from .models import Post, Comment #new
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment) #new
