from django.urls import path
from .views import (
    signup,
    profile,
)

urlpatterns = [
    path('signup/', signup),
    path('<int:user_pk>/', profile),
]
