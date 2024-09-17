from django.contrib import admin

# blog/admin.py
from .models import Post

admin.site.register(Post)