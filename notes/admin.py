from django.contrib import admin

# Register your models here.

from .models import Album ,Song, users

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(users)
