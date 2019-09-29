from django.urls import path, re_path
from .views import SlideshowListAPIView


urlpatterns = [
    path('slideshow/', SlideshowListAPIView.as_view()),
]