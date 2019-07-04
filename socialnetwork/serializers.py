from rest_framework import serializers
from .models import User,Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ('first_name', 'last_name', 'mail', 'password', 'average', 'relationships')
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,read_only=True)
    class Meta:
        model = Post
        fields = ('created_at', 'text', 'photo', 'user')



