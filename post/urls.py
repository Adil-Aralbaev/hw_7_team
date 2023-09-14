from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView, PostRetrieveUpdateDestroyAPIView, PostListCreateAPIView, rating_create_api_view, create_post_api_view

urlpatterns = [
    # path('', PostListCreateAPIView.as_view()),
    path('', create_post_api_view),

    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('comment/', CommentListCreateAPIView.as_view()),
    path('comment/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view()),
    # path('<int:pk>/comment', DetailCommentListCreateAPIView.as_view()),

    path('rating/', rating_create_api_view),
]