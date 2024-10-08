
from django.urls import path
from .views import NewsApiView,CategoryApiView,CommentApiView

urlpatterns = [
    path('news/', NewsApiView.as_view()),
    path('news/<int:pk>/', NewsApiView.as_view()),
    path('category/', CategoryApiView.as_view()),  # new path
    path('category/<int:pk>/', CategoryApiView.as_view()),  # new path
    path('comment/', CommentApiView.as_view()),  # new path
    path('comment/<int:pk>/', CommentApiView.as_view()),  # new path
]
