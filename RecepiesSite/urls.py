from django.urls import path
from RecepiesSite.views.home import index
from RecepiesSite.views.recipe_view import recipe_view, add_recipe, edit_recipe, delete_recipe, AdminRecipeView
from RecepiesSite.views.email_newsletter import email_list_signup
from RecepiesSite.views.search_view import searchview

urlpatterns = [
    path('', index, name='index'),
    path('subscribe/', email_list_signup, name='subscribe'),
    path('recipe/<int:pk>', recipe_view, name='recipe'),
    path('search/', searchview, name='search'),
    path('add/', add_recipe, name='add recipe'),
    # path('add/', RecipeCreateView.as_view(template_name='add_recipe.html', ), name='add recipe'),
    path('recipe/<int:pk>/edit', edit_recipe, name='recipe-update'),
    path('recipe/<int:pk>/delete', delete_recipe, name='recipe-delete'),
    path('recipeslist/', AdminRecipeView.as_view(), name='admin-recipes'),

]
