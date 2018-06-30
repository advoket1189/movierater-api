from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from movierater.api import views
from movierater.api.views import CustomAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authenticate/', CustomAuthToken.as_view()),
]