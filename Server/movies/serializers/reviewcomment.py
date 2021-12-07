from rest_framework import serializers
from ..models import Reviewcomment


class ReviewcommentSerializer(serializers.ModelSerializer):
    '''
    리뷰 댓글 생성 / 수정 (리뷰 댓글이 가지고 있는 모든 정보)
    '''
    class Meta:
        model = Reviewcomment
        fields = '__all__'
        read_only_fields = ('review', 'user', 'username', )