from rest_framework import serializers
from rest_framework.authtoken import models
from statistics import mean


from .models import Post, Comment, Rating

#
# class PostSerializer(serializers.ModelSerializer):
#     username = serializers.SerializerMethodField()
#     rating = serializers.SerializerMethodField(default=0)
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#         read_only_fields = ['user', ]
#
#     def get_username(self, obj):
#         return obj.user.username
#
#     def get_rating(self, obj):
#         return obj.user.rating
#

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user', 'average_rating']

    def get_username(self, obj):
        return obj.user.username

    def get_average_rating(self, obj):

        # ratings = Rating.objects.values_list(post=obj.id)
        ratings = Rating.objects.filter(post=obj.id).values()
        print(type(ratings))
        r_list = []
        for r in ratings:
            r_list.append(r['rating'])

        print(ratings)
        if ratings.exists():
            average = round(mean(r_list), 2)
            # average = ratings.aggregate(models.Avg('rating'))['rating__avg']
            return average
        return 0


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', ]

    def get_username(self, obj):
        return obj.user.username


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['user', ]
