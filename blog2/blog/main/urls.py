from django.urls import path
from .views import KlassAPIView, KlassDetailAPIView, MexmonxonaAPIView, MexmonxonaDetailAPIView, TravelAPIView, TravelDetailAPIView

urlpatterns = [
    path('klass/', KlassAPIView.as_view(), name='klass-list'),
    path('klass/<int:pk>/', KlassDetailAPIView.as_view(), name='klass-detail'),
    path('mexmonxona/', MexmonxonaAPIView.as_view(), name='mexmonxona-list'),
    path('mexmonxona/<int:pk>/', MexmonxonaDetailAPIView.as_view(), name='mexmonxona-detail'),
    path('travel/', TravelAPIView.as_view(), name='travel-list'),
    path('travel/<int:pk>/', TravelDetailAPIView.as_view(), name='travel-detail'),
]
