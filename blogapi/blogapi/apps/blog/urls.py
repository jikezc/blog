from django.urls import path, re_path
from .views import ArticleCategroyListAPIView

urlpatterns = [
    path('categroy/', ArticleCategroyListAPIView.as_view())
]
