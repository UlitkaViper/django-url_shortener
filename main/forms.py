from django import forms
from .models import URL


class UrlField(forms.ModelForm):
    full_url = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'url_to_short',
               'id': 'textarea'}), max_length=150)

    class Meta:
        model = URL
        fields = ['full_url']
