from django import forms


class PaidForm(forms.Form):
    name = forms.CharField(max_length=50, label='')

    def clean(self):
        print(self.kwarg)
        return self.cleaned_data
