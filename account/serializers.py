from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'telegram_chat_id', 'is_staff', 'password', 'email']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            telegram_chat_id=validated_data['telegram_chat_id']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


#
# class StaffUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StaffUser
#         fields = '__all__'
#         write_only_fields = ['password', ]
