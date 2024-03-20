from django.shortcuts import render

from .forms import ContestForm
from .models import Contest


def proposal(request):
    form = ContestForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    ice_creams = Contest.objects.all().order_by('id')
    context = { 'ice_creams': ice_creams}
    return render(request, 'contest/contest_list.html', context)
