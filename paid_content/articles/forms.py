from django import forms


class PaidForm(forms.Form):
    accept = forms.BooleanField(label='Согласен на оформление платной подписки:')
