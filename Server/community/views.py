from django.shortcuts import (
    get_object_or_404,
)
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from .serializers import (
    ArticleListSerializer,
    ArticleSerializer,
    CommentSerializer,
)
from .models import (
    Article,
    Comment,
)
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['GET'])
def article_list(request):
    '''
    GET: 게시글 리스트 가져오기
    '''
    if request.method == 'GET':
        articles = Article.objects.order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    '''
    POST: 게시글 작성하기
    '''
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        user = User.objects.get(pk=request.data['user'])
        username = user.username
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, username=username)
            return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['GET'])
def article_detail(request, article_pk):
    '''
    GET: 게시글 상세정보
    '''
    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_update_delete(request, article_pk):
    '''
    PUT: 게시글 수정
    DELETE: 게시글 삭제
    '''
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        article.delete()
        return Response(
            data = {'message': f'{article_pk}번 게시글이 삭제되었습니다.'},
            status=HTTP_204_NO_CONTENT
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    '''
    POST: 댓글 작성
    '''
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    user = User.objects.get(pk=request.data['user'])
    username = user.username
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=user, username=username)
        return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, comment_pk):
    '''
    PUT: 댓글 수정
    DELETE: 댓글 삭제
    '''
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    elif request.method == 'DELETE':
        comment.delete()
        return Response(
            data = { 'message': f'{comment_pk}번 댓글이 삭제되었습니다.' },
            status=HTTP_204_NO_CONTENT
        )

