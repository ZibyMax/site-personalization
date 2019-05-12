from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', primary_key=True)
    is_paid_access = models.BooleanField(default=False, verbose_name='Расширенная подписка')

    def __str__(self):
        suffix = ' +' if self.is_paid_access else ''
        return f'{self.user.username}{suffix}'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    picture = models.CharField(max_length=200, verbose_name='Тематическое изображение')
    content = models.TextField(verbose_name='Текст статьи')
    is_paid_access = models.BooleanField(default=False, verbose_name='Платный доступ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
