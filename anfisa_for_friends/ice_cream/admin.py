from django.contrib import admin

from .models import (
    Category, IceCream, Topping, Wrapper
)


class IceCreamAdmin(admin.ModelAdmin):
    """Класс для настройки страницы админа."""
    # Поля будут показаны на странице списка объектов.
    list_display: tuple[str] = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
    )
    # Поля можно редактировать прямо на странице
    # списка объектов.
    list_editable: tuple[str] = (
        'is_published',
        'is_on_main',
        'category',
    )
    # Поля по которым будет проводиться поиск.
    search_fields: tuple[str] = ('title',)
    # Поля по которым можно фильтровать записи.
    list_filter: tuple[str] = ('category',)
    # Поля, при клике на которые можно перейти
    # на страницу просмотра и редактирования записи.
    list_display_links: tuple[str] = ('title',)
    # Вместо пустого значения будет выводиться строка
    # "Не задано".
    empty_value_display: str = 'Не задано'
    # Для каких связных полей интерфейс будет
    # "два окна".
    filter_horizontal: tuple[str] = ('toppings',)


# Подготовка модели IceCream для вставки на страницу
# другой модели.
class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra: int = 2


class CategoryAdmin(admin.ModelAdmin):
    inlines: tuple = (
        IceCreamInline,
    )
    list_display: tuple[str] = (
        'title',
    )


# Регистрируем приложения.
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
