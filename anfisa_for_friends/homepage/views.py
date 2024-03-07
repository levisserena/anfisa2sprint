from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template: str = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
    ).filter(
        Q(is_published=True)
        & (Q(is_on_main=True) | Q(title__contains='пломбир'))
    ).order_by('title')[1:4]
    context: dict[str:any] = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
