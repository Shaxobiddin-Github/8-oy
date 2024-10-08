from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class News(models.Model):
    title = models.CharField(max_length=100)
    deskription = models.TextField()
    image = models.ImageField(upload_to='authors/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    muallif = models.CharField(max_length=255)


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f'Comment by {self.name} on {self.news.title}'
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='authors/', null=True, blank=True)