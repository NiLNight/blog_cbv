from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from apps.blog.models import Post, Category


@admin.register(Post)
class PostAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели записей
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}
