from django.contrib import admin

# Register your models here.
from .models import Category, News, Comment, Author

admin.site.register(Category)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'deskription', 'category')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'name', 'comment', 'email')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    

