from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.forms import model_to_dict

from .models import Category, News, Comment,Author


class NewsApiView(APIView):
    def get(self, request:Request,pk=None):
        if not pk:

            new_list = []
            news = News.objects.all()
            
            for new in news:
                new_list.append({
                    'id': new.id,
                    'title': new.title,
                    'description': new.deskription,
                    'created_at': new.created_at,
                    'category_id': new.category.id,
                    'category_name': new.category.name,
                    'muallif':new.muallif,
                    'image': new.image.url if new.image else None,
                    # 'comments': [comment.id for comment in new.comment.all()],
                        
                })

            return Response(new_list)
        try:
            car = News.objects.get(pk=pk)
            return Response(model_to_dict(new))
        except:
            return Response({'error': 'Car not found'})

class CommentApiView(APIView):
    def get(self, request:Request, pk=None):
        if not pk:
            new_list = []
            comments = Comment.objects.all()
            
            for comment in comments:
                new_list.append({
                    'id': comment.id,
                    'news_id': comment.news.id,
                    'name': comment.name,
                    'comment': comment.comment,
                    'created_at': comment.created_at,
                    'email': comment.email,
                        
                })

            return Response(new_list)
        
        try:
            comment = Comment.objects.get(pk=pk)
            return Response(model_to_dict(comment))
        except:
            return Response({'error': 'Comment not found'})
        

class CategoryApiView(APIView):
    def get(self, request:Request, pk=None):
        if not pk:
            new_list = []
            categories = Category.objects.all()
            
            for category in categories:
                new_list.append({
                    'id': category.id,
                    'name': category.name,
                    'image': category.image.url if category.image else None,
                        
                })

            return Response(new_list)
        try:
            category = Category.objects.get(pk=pk)
            return Response(model_to_dict(category))
        except:
            return Response({'error': 'Category not found'})
        
class AuthorApiView(APIView):
    def get(self, request:Request, pk=None):
        if not pk:
            new_list = []
            authors = Author.objects.all()
            
            for author in authors:
                new_list.append({
                    'id': author.id,
                    'name': author.name,
                    'bio': author.bio,
                    'image': author.image.url if author.image.url else None,
                        
                })

            return Response(new_list)
        try:
            author = Author.objects.get(pk=pk)
            return Response(model_to_dict(author))
        except:
            return Response({'error': 'Author not found'})