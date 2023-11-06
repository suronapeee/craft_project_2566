from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        #print(type(self.id)) # <class 'int'>
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    comment_text = models.CharField(max_length=100)
    user_rating = models.IntegerField()
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    is_approved = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text