from django.shortcuts import render

from .forms import ContestForm


def proposal(request):
    form = ContestForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        pass
    return render(request, 'contest/form.html', context)
