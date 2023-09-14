from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BaseAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, AllowAny, IsAdminUser
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


# class UserListCreateAPIView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAdminPermission]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


@api_view(http_method_names=['GET', 'POST'])
@authentication_classes([TokenAuthentication, ])
def user_list_create_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # if serializer.data.name.startswith('adm'):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [BasePermission]


# class StaffUserListCreateAPIView(ListCreateAPIView):
#     queryset = StaffUser.objects.all()
#     serializer_class = StaffUserSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [BasePermission]
#
#
# class StaffUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = StaffUser.objects.all()
#     serializer_class = StaffUserSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [BasePermission]
