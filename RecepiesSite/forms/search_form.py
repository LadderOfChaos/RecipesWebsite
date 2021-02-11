from django import forms

from RecepiesSite.Models.recipe import Recipe


class SearchForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title']
