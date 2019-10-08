from django.urls import path, re_path
from .views import ArticleCategroyListAPIView, AriclePostListAPIView

urlpatterns = [
    path('', AriclePostListAPIView.as_view()),
    path('categroy/', ArticleCategroyListAPIView.as_view()),
]
