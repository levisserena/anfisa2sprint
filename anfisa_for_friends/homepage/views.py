from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id',
        'title',
        'price',
        'description',
    ).filter(
        (Q(is_published=True) & Q(category__is_published=True))
        & (Q(is_on_main=True) | Q(title__contains='Кракозябра'))
    ).order_by('title')[0:3]
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
