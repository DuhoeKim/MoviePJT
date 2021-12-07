from rest_framework import serializers
from ..models import Movie, Moviecomment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', )


class MovieListSerializer(serializers.ModelSerializer):
    '''
    모든 영화 데이터 조회
    '''
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', )



class MovieSerializer(serializers.ModelSerializer):
    '''
    영화 상세 정보 (영화가 가지고 있는 모든 데이터 + 영화에 대한 한줄평 데이터)
    '''
    like_users = UserSerializer(many=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)
    
    class MoviecommentListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Moviecomment
            fields = '__all__'

    genres = serializers.StringRelatedField(many=True)

    moviecomment_set = MoviecommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'