from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from RecepiesSite.Models.recipe import Recipe
from RecepiesSite.forms.RecipeForm import RecipeForm, DeleteRecipeForm
from RecepiesSite.forms.email_sub_form import EmailSignupForm
from django.views.generic import ListView


def recipe_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    list_ingredients = recipe.ingredients.split(',')
    if request.method == "GET":
        context = {
            'recipe': recipe,
            'list_ingredients': list_ingredients,
            'can_edit': request.user == recipe.author.user or request.user.is_superuser,
            'can_delete': request.user == recipe.author.user or request.user.is_superuser,
            'more_recipes': Recipe.objects.filter(author=recipe.author).order_by('-author')[:4]
        }
        return render(request, 'single-page.html', context)
    else:
        return redirect('index')


def add_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        e_form = EmailSignupForm()
        context = {
            'form': form,
            'e_form': e_form,
        }
        return render(request, 'add_recipe.html', context)
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe', recipe.pk)
        context = {
            'form': form,
            'e_form': EmailSignupForm(),
            'recipe': Recipe.objects.filter(author__user__username="stefan").order_by('-type')[:4],
            'recipe_date': Recipe.objects.order_by("-date")[:4],
            'bg_recipe': Recipe.objects.filter(type='Bulgarian').order_by('-type')[:4],
            'world_recipe': Recipe.objects.filter(type='Worldwide').order_by('-type')[:4],
        }
        return render(request, 'index.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        form = RecipeForm(instance=recipe)
        context = {
            'form': form,
            'recipe': recipe,
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid() and request.user == recipe.author.user or request.user.is_superuser:
            form.save()
            return redirect('recipe', recipe.pk)
        context = {
            'form': form,
            'recipe': recipe,
        }
        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'recipe': recipe,
            'form': DeleteRecipeForm(instance=recipe),
        }
        return render(request, 'delete.html', context)
    else:
        if request.user == recipe.author.user or request.user.is_superuser:
            recipe.delete()
            return redirect('index')
        return redirect('index')



class AdminRecipeView(ListView):
    model = Recipe
    template_name = 'admin-list.html'
    context_object_name = 'recipe'
    ordering = ['-date']
    paginate_by = 10

