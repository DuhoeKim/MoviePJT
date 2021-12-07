from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    PofileSerializer,
)
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['POST'])
def signup(request):
    '''
    POST: 회원가입 기능
    '''
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')

    if password != password_confirmation:
        return Response({
            'message': ['비밀번호가 일치하지 않습니다.']
        }, HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data) # serializer instance
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password) # 암호화 (hashing) 작업
        user.save()
    return Response(serializer.data, HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, user_pk):
    if request.method == 'GET':
        person = get_object_or_404(User, pk=user_pk)
        serializer = PofileSerializer(person)
        return Response(serializer.data)