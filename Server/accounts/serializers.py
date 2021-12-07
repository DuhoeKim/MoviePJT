from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password', )


class PofileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    like_movies = MovieSerializer(many=True)
    like_movies_count = serializers.IntegerField(source='like_movies.count', read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'like_movies', 'like_movies_count', )