from django import forms

from .models import Contest

TEXTAREA = {'cols': '22', 'rows': '5'}


class ContestForm(forms.ModelForm):

    class Meta:
        model = Contest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(TEXTAREA),
            'comment': forms.Textarea(TEXTAREA),
        }
