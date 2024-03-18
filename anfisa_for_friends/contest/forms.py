from django import forms


class ContestForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20)
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            {'cols': '30', 'rows': '5'},
        )
    )
    price = forms.DecimalField(
        label='Цена',
        min_value=10,
        max_value=100,
        help_text='Рекомендованная розничная цена'
    )
    comment = forms.CharField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea(
            {'cols': '30', 'rows': '5'},
        ),
    )
