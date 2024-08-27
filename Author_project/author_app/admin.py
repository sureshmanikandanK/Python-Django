from django.contrib import admin

# Register your models here.
from .models import*
admin.site.register(Author)
admin.site.register(TagLine)
admin.site.register(Comment)
admin.site.register(Post)