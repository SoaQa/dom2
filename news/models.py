from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse

from dom2.settings import MEDIA_URL


class Novelty(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", null=False, blank=True)
    image = models.FileField(upload_to='images/', unique=True, verbose_name='Картинка', null=True, blank=True)
    text = models.TextField(verbose_name="Текст статьи")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.title}: {self.creator.username}'

    @property
    def image_url(self):
        return MEDIA_URL + self.image.name
