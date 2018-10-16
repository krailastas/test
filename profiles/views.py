import hashlib

from rest_framework import mixins, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from profiles.models import User
from .serializers import LoginSerializer


class LoginViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
            **LoginViewSet**

            Return token.

    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.data['code']
        md_key = hashlib.md5(code.encode()).hexdigest()
        qs = User.objects.filter(code=md_key)
        if qs.exists():
            obj = qs[0]
            Token.objects.filter(user=obj).delete()
            token = Token.objects.create(user=obj)
            data = {
                'id': obj.id,
                'token': token.key
            }
            headers = self.get_success_headers(serializer.data)
            return Response(data, status=status.HTTP_200_OK,
                            headers=headers)
        else:
            return Response(
                {'errors': 'Your code is invalid.'},
                status=status.HTTP_400_BAD_REQUEST
            )
