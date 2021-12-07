from django.urls import path
from .views import (
    article_list,
    article_create,
    article_detail,
    article_update_delete,
    comment_create,
    comment_update_delete,
)

urlpatterns = [
    path('articles/', article_list),
    path('articles/create/', article_create),
    path('articles/detail/<int:article_pk>/', article_detail),
    path('articles/<int:article_pk>/', article_update_delete),
    path('articles/<int:article_pk>/comments/', comment_create),
    path('comments/<int:comment_pk>/', comment_update_delete),
]
