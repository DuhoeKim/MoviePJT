from rest_framework import serializers
from ..models import Moviecomment


class MoviecommentSerializer(serializers.ModelSerializer):
    '''
    영화 한줄평 생성 / 수정 (영화 한줄평이 가지고 있는 모든 정보)
    '''

    class Meta:
        model = Moviecomment
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'username', )