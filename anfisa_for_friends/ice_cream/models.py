from django.db import models

from core.models import PublishedModel, TitleModel


class Category(PublishedModel, TitleModel):
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Слаг',
    )
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Topping(PublishedModel, TitleModel):
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Слаг',
    )

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'


class Wrapper(PublishedModel, TitleModel):

    class Meta:
        verbose_name = 'Обёртка'
        verbose_name_plural = 'Обёртки'


class IceCream(PublishedModel, TitleModel):
    description = models.TextField(
        verbose_name='Описание',
    )
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обёртка',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория',
    )
    toppings = models.ManyToManyField(
        Topping,
        verbose_name='Топпинги',
    )
    is_on_main = models.BooleanField(
        default=False,
        verbose_name='На главную',
    )

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
