from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body =  RichTextField(blank=True,null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post')
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog_detail', args=(str(self.id)))

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, related_name='commenter', on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post.title) + ' | ' + self.comment

class Reply(models.Model):
    parent_comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    replier = models.ForeignKey(User, related_name='replier', on_delete=models.CASCADE)
    reply = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.parent_comment) + ' -Reply- ' + self.reply