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
        help_text='Уникальное название, не более 256 символов',
    )

    class Meta:
        abstract = True

    # Вывод записей, чтобы в качестве заголовка показывалось название.
    def __str__(self):
        return self.title


class SlugModel(models.Model):
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Слаг',
        help_text='Slug - это сокращенная метка для чего '
                  '- либо, содержащая только латинские буквы, '
                  'цифры, подчеркивания или дефисы.',
    )

    class Meta:
        abstract = True
