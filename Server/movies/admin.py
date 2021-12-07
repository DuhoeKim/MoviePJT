from django.contrib import admin
from .models import (
    Movie,
    Moviecomment,
    Review,
    Reviewcomment,
)

admin.site.register(Movie)
admin.site.register(Moviecomment)
admin.site.register(Review)
admin.site.register(Reviewcomment)