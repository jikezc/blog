from django.urls import path, re_path
from .views import ArticleCategroyListAPIView, ArticlePostListAPIView, ArticleRetrieveAPIView, MessagesListAPIView, MessagesCreateAPIView

urlpatterns = [
    path('', ArticlePostListAPIView.as_view()),
    path('categroy/', ArticleCategroyListAPIView.as_view()),
    re_path('(?P<pk>\d+)/', ArticleRetrieveAPIView.as_view()),
    path('messages/', MessagesListAPIView.as_view()),
    path('send_messages/', MessagesCreateAPIView.as_view()),
]
