from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published."""
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
    )

    class Meta:
        abstract = True


class TitleModel(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
