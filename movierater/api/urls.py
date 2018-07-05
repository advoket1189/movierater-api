from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
import movierater.api
from movierater.api.views import CustomAuthToken

router = routers.DefaultRouter()
router.register(r'users', movierater.api.views.UserViewSet)
router.register(r'groups', movierater.api.views.GroupViewSet)
router.register(r'movies', movierater.api.views.MovieViewSet)
router.register(r'rating', movierater.api.views.RatingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authenticate/', CustomAuthToken.as_view()),
]
