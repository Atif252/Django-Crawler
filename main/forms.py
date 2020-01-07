from django import forms


class UrlForm(forms.Form):
    url = forms.URLField()

    class Meta:
        fields = ('url',)
