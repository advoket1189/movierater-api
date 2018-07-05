from typing import Tuple

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Movie(models.Model):
    objects = None
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=150)


class Rating(models.Model):
    objects = None
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Meta:
    unique_together = (('user', 'movie'),)
    index_together: Tuple[Tuple[str, str]] = (('user', 'movie'),)
