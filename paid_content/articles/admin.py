from django.contrib import admin
from .models import Profile, Article


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid_access')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'content', 'is_paid_access')


admin.site.register(Profile, ProfileAdmin)

admin.site.register(Article, ArticleAdmin)