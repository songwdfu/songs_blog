from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime

# define publish status
STATUS = (
        (0, "Draft"),
        (1, "Publish")
)

# define post class with attributes (fields)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # nested metadata class
    class Meta:
        ordering = ['-created_on']

    # for display
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            self.status = 1
        super(Post, self).save(*args, **kwargs)

    # def publish(self, *args, **kwargs):
    #     if self.status == 0:
    #         self.status = 1
