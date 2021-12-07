from django.urls import path
from .views import (
    movies_list,
    movie_detail,
    movie_like,
    movie_comment_create,
    movie_comment_update_delete,
    review_list,
    review_create,
    review_detail,
    review_update_delete_comment_create,
    review_comment_update_delete,
    recommend,
)

urlpatterns = [
    path('', movies_list),
    path('<int:movie_pk>/', movie_detail),
    path('<int:movie_pk>/like/', movie_like),
    path('<int:movie_pk>/comment_create/', movie_comment_create),
    path('<int:movie_comment_pk>/comment_update_delete/', movie_comment_update_delete),
    path('<int:movie_pk>/review/', review_list),
    path('<int:movie_pk>/review/create/', review_create),
    path('<int:review_pk>/review/detail/', review_detail),
    path('<int:review_pk>/review/update_delete_comment_create/', review_update_delete_comment_create),
    path('<int:review_comment_pk>/review/review_comment_update_delete/', review_comment_update_delete),
    path('<int:user_pk>/recommend/', recommend),

]
