from django.contrib import admin
from movierater.api.models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    List_display = ['title', 'description']
    search_fields = ('title', 'description')