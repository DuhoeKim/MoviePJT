from django.contrib.auth import get_user_model
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.response import Response
from .models import (
    Movie,
    Moviecomment,
    Review,
    Reviewcomment,
    Credit,
)
from .serializers.movie import (
    MovieSerializer,
    MovieListSerializer,
)
from .serializers.moviecomment import (
    MoviecommentSerializer,
)
from .serializers.review import (
    ReviewSerializer,
    ReviewListSerializer,
)
from .serializers.reviewcomment import (
    ReviewcommentSerializer,
)
from .serializers.credit import (
    CreditSerializer,
)
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['GET'])
def movies_list(request):
    '''
    GET: 전체 영화 정보 가져오기
    '''
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    '''
    GET: 영화 상세 데이터 (댓글 정보 포함)
    '''
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    '''
    POST: 좋아요 하기 / 취소
    '''
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = User.objects.get(pk=request.data['user'])
    if movie.like_users.filter(pk=request.data['user']).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_comment_create(request, movie_pk):
    '''
    POST: 한줄평 작성
    '''
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MoviecommentSerializer(data=request.data)
        user = User.objects.get(pk=request.data['user']) # user_id에 맞는 user 인스턴스
        username = user.username # user data 중 username
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user, username=username)
            return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def movie_comment_update_delete(request, movie_comment_pk):
    '''
    PUT: 한줄평 수정
    DELETE: 한줄평 삭제
    '''
    movie_comment = get_object_or_404(Moviecomment, pk=movie_comment_pk)

    if request.method == 'PUT':
        serializer = MoviecommentSerializer(instance=movie_comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        movie_comment.delete()
        return Response(data='한줄평이 삭제되었습니다.', status=HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_list(request, movie_pk):
    '''
    GET: 영화와 관련된 리뷰 리스트
    '''
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        reviews = movie.review_set.order_by('-pk')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    '''
    POST: 리뷰 작성
    '''
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        user = User.objects.get(pk=request.data['user']) # user_id에 맞는 user 인스턴스
        username = user.username # user data 중 username
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user, username=username)
            return Response(serializer.data)


@api_view(['GET'])
def review_detail(request, review_pk):
    '''
    GET: 리뷰 상세 조회
    '''
    if request.method == 'GET':
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_update_delete_comment_create(request, review_pk):
    '''
    POST: 리뷰에 댓글 작성
    PUT: 리뷰 수정
    DELETE: 리뷰 삭제
    '''
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'POST':
        serializer = ReviewcommentSerializer(data=request.data)
        user = User.objects.get(pk=request.data['user']) # user_id에 맞는 user 인스턴스
        username = user.username # user data 중 username
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=user, username=username)
            return Response(serializer.data, status=HTTP_201_CREATED)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(data='리뷰가 삭제되었습니다.', status=HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_comment_update_delete(request, review_comment_pk):
    '''
    PUT: 리뷰 댓글 수정
    DELETE: 리뷰 댓글 삭제
    '''
    review_comment = get_object_or_404(Reviewcomment, pk=review_comment_pk)

    if request.method == 'PUT':
        serializer = ReviewcommentSerializer(instance=review_comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review_comment.delete()
        return Response(data='댓글이 삭제되었습니다.', status=HTTP_204_NO_CONTENT)


@api_view(['GET'])
def recommend(request, user_pk):
    if request.method == 'GET':
        # user가 좋아요한 영화 가져오기
        user = User.objects.get(pk=user_pk)
        visited = [0] * 19
        # genre id 저장
        genres_name_list = (
            12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99,
            878, 9648, 10402, 10749, 10751, 10752, 10770
        )
        like_movies = user.like_movies.all()
        if not len(like_movies):
            return Response({
                'message': '좋아요한 영화가 없습니다.'
                }, status=HTTP_204_NO_CONTENT
            )
        temp_genres = []
        for like_movie in like_movies:
            like_genres = like_movie.genres.all() # 좋아요한 영화들의 장르 가져오기
            for like_genre in like_genres:
                temp_genres.append([like_genre.id, len(like_genres)]) # 장르 아이디를 저장

        cast_list = [] # 출연진 리스트
        crew_list = [] # 연출진 리스트
        for i in range(len(like_movies)):
            credit = Credit.objects.get(pk=like_movies[i].pk)
            serializer = CreditSerializer(credit)
            # 관계자들의 이름만 저장
            for j in range(len(serializer.data['cast'])):
                cast_list.append(serializer.data['cast'][j]['name'])
            for j in range(len(serializer.data['crew'])):
                crew_list.append(serializer.data['crew'][j]['name'])
        cast_list = list(set(cast_list))
        crew_list = list(set(crew_list))
        # 가장 많이 나온 장르 뽑아내기
        i = 0
        weight = 1 # 가중치(좋아요를 누른 순서대로 큰 가중치를 가짐)
        while i < len(temp_genres):
             # 장르 아이디가 있는 인덱스에 맞춰 장르의 개수로 나눈 값에 * 가중치
            visited[genres_name_list.index(temp_genres[i][0])] += round(1 / temp_genres[i][1] * weight, 3)
            if i < 3:
                weight -= 0.2
            i += 1
        best_movies = []
        while True:
            target_genre_id = genres_name_list[visited.index(max(visited))] # 최대 visited 값에 맞는 장르 아이디
            visited[visited.index(max(visited))] = 0
            # 얻은 장르 아이디로 관련 영화 뽑아내기
            target_movies = Movie.objects.filter(genres__pk=target_genre_id)
            temp_movies = []

            for target_movie in target_movies:
                target_movie_credit = Credit.objects.get(pk=target_movie.pk)
                serializer = CreditSerializer(target_movie_credit)
                cast_score = 10 # 기본 값
                crew_score = 10
                for i in range(len(serializer.data['cast'])):
                    if serializer.data['cast'][i]['name'] in cast_list:
                        cast_score += 8
                for j in range(len(serializer.data['crew'])):
                    if serializer.data['crew'][j]['name'] in crew_list:
                        crew_score += 6
                
                # 득표 점수의 신뢰도 향상을 위해 평균과 총 득표수, 출연, 연출진의 정보 값을 곱해준다.
                score = target_movie.vote_count * target_movie.vote_average * cast_score * crew_score
                temp_movies.append([score, target_movie.pk])

            temp_movies.sort(key=lambda x: x[0], reverse=True) # 점수 기준 정렬
            print(len(target_movies), target_genre_id)
            i = 0
            flag = False
            while len(best_movies) < 10:
                # 10개의 영화를 못 고른 경우 다음 점수가 높은 장르를 선택하러 고고!
                if(i>=len(temp_movies)):
                    flag = True
                    break
                best_movie = Movie.objects.get(pk=temp_movies[i][1])
                if best_movie in like_movies:
                    i += 1
                    continue
                serializer = MovieSerializer(best_movie)
                best_movies.append(serializer.data)
                i += 1
            if flag:
                continue
            return Response(best_movies)