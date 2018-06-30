from django.contrib.auth.models import User, Group
from django.template.base import Token
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from movierater.api.serializers import UserSerializer, GroupSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from movierater.api.models import Movie
from movierater.api.serializers import MovieSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    class MovieViewSet(viewsets.ModelViewSet):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        authentication_classes = (TokenAuthentication, SessionAuthentication,)
        permission_classes = (IsAuthenticated,)


class CustomObtainAuthToken(object):
    pass


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.object.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many=False)
        return Response({'token': token.key, 'user': serializer.data})


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer