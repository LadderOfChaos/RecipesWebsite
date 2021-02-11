from RecepiesSite.Models.recipe import Recipe
from RecepiesSite.Models.search import Search
from django.shortcuts import render

from RecepiesSite.forms.search_form import SearchForm


def searchview(request):
    form = SearchForm(request.GET or None)
    context = {}
    if request.method == "GET":
        if form.is_valid():
            queryset = Recipe.objects.filter(title__icontains=request.GET.get("title"))
            context = {
                'queryset': queryset,
            }

    return render(request, 'search-recipe.html',context)