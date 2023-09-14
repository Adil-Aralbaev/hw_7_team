from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'telegram_chat_id', 'email' ]
        # read_only_fields = ['is_staff', ]
        # write_only_fields = ['password', ]

#
# class StaffUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StaffUser
#         fields = '__all__'
#         write_only_fields = ['password', ]
