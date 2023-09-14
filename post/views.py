import requests
from django.shortcuts import render
from django_rest.permissions import AllowAny
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, RatingSerializer


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [BasePermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [BasePermission]


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [BasePermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class DetailCommentListCreateAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [BasePermission]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user, post=self.request.post)


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [BasePermission]


@api_view(http_method_names=['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny, ])
def rating_create_api_view(request):
    user = request.user
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(http_method_names=['POST', 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def create_post_api_view(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            def send_telegram_message(bot_message):
                bot_token = '6275876428:AAG0l9_8h4c5m_h-SsH0hdvq-7-YVRnt-nU'
                bot_chat_id = request.user.telegram_chat_id
                send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={bot_message}'
                response = requests.get(send_text)
                response.json()
            serializer.save(user=request.user)
            post_title = serializer.validated_data.get('title', '')
            post_body = serializer.validated_data.get('body', '')
            send_telegram_message(f'Пост с названием "{post_title}" и текстом "{post_body}" успешно создан')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(data=posts, many=True)
        serializer.is_valid()
        return Response(serializer.data)