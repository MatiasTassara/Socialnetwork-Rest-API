from django.contrib import admin
from .models import User,Relationship,Post,Comment

admin.site.register(User)
admin.site.register(Relationship)
admin.site.register(Post)
admin.site.register(Comment)
