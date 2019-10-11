from django.urls import path, re_path
from .views import ArticleCategroyListAPIView, ArticlePostListAPIView, ArticleRetrieveAPIView, MessagesListAPIView, \
    MessagesCreateAPIView, HomeArticleListAPIView, GiveLikeRetrieveUpdateAPIView

urlpatterns = [
    path('', ArticlePostListAPIView.as_view()),
    path('categroy/', ArticleCategroyListAPIView.as_view()),
    re_path(r'^(?P<pk>\d+)/', ArticleRetrieveAPIView.as_view()),
    path('messages/', MessagesListAPIView.as_view()),
    path('send_messages/', MessagesCreateAPIView.as_view()),
    path('three/', HomeArticleListAPIView.as_view()),
    re_path('^give_like/(?P<pk>\d+)/', GiveLikeRetrieveUpdateAPIView.as_view()),
]
