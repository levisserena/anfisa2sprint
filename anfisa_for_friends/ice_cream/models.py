from django.db import models

from core.models import PublishedModel, SlugModel, TitleModel


class Category(PublishedModel, TitleModel, SlugModel):
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения',
        help_text='Порядок отображения. По умолчанию 100.'
                  'Чем ниже значение, тем выше будет отображаться.',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Topping(PublishedModel, TitleModel, SlugModel):

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'


class Wrapper(PublishedModel, TitleModel):

    class Meta:
        verbose_name = 'Обёртка'
        verbose_name_plural = 'Обёртки'


class IceCream(PublishedModel, TitleModel):
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения',
        help_text='Порядок отображения. По умолчанию 100.'
                  'Чем ниже значение, тем выше будет отображаться.',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    price = models.DecimalField(
        max_digits=6,      # Количество цифр, допустимых в числе.
        decimal_places=2,  # Количество цифр, после запятой.
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
        help_text='Чтобы отображалось на главной '
                  'странице поставь галочку',
    )

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
