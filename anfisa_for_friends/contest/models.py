from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db import models


class Contest(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=20
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    price = models.IntegerField(
        verbose_name='Цена',
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100),
        ],
        help_text='Рекомендованная розничная цена'
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
    )
