from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Post(models.Model):
    tittle = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Author")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts", verbose_name="Category")
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True, verbose_name="Tags")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Published at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.tittle
    
    class Meta:
        ordering = ['-published_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"