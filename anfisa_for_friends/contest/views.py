from django.shortcuts import render


def proposal_create(request):
    return render(request, 'contest/form.html')


def accepted(request):
    return render(request, 'contest/proposal_accepted.html')
