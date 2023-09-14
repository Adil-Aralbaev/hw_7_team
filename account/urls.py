from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import user_list_create_api_view, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('user/', user_list_create_api_view),
    path('user/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    # path('staff_user/', StaffUserListCreateAPIView.as_view()),
    # path('staff_user/<int:pk>', StaffUserRetrieveUpdateDestroyAPIView.as_view()),

]