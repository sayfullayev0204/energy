from django import forms
from .models import EnergiyaSarfi

class EnergiyaSarfiForm(forms.ModelForm):
    oy = forms.ChoiceField(
        choices=EnergiyaSarfi._meta.get_field('oy').choices,  # Modeldan choice list olamiz
        widget=forms.Select(attrs={'class': 'form-select border-success'})
    )

    class Meta:
        model = EnergiyaSarfi
        fields = ['mahalla', 'oy', 'yil', 'elektr_kVt', 'gaz_m3', 'suv_m3']
