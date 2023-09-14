from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView, PostRetrieveUpdateDestroyAPIView, PostListCreateAPIView

urlpatterns = [
    path('post/', PostListCreateAPIView.as_view()),
    path('post/<int:pk>/', PostListCreateAPIView.as_view()),
    path('comment/', CommentListCreateAPIView.as_view()),
    path('comment/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('post/<int:pk>/comment', PostListCreateAPIView.as_view()),

]