from rest_framework import serializers
from ..models import Review, Reviewcomment



class ReviewcommentListSerializer(serializers.ModelSerializer):
    '''
    리뷰 전체 목록
    '''
    class Meta:
        model = Reviewcomment
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'username', )


class ReviewListSerializer(serializers.ModelSerializer):
    reviewcomment_set = ReviewcommentListSerializer(many=True, read_only=True)
    reviewcomment_count = serializers.IntegerField(source='reviewcomment_set.count', read_only=True)
    class Meta:
        model = Review
        exclude = ('content', )



class ReviewSerializer(serializers.ModelSerializer):
    '''
    리뷰 상세 목록 (리뷰 전체 데이터와 그 리뷰에 달려있는 댓글들)
    '''
    reviewcomment_set = ReviewcommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'username', )