from django import forms
from .models import Sneaker


class SneakerForm(forms.ModelForm):
    class Meta:
        model = Sneaker
        fields = ('name', 'brand', 'description', 'link', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
        }
