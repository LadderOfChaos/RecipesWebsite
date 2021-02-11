from django.contrib import admin
from RecepiesSite.Models.recipe import Recipe
from RecepiesSite.Models.email_sub import Signup
from RecepiesSite.Models.search import Search



admin.site.register(Recipe)
admin.site.register(Signup)
admin.site.register(Search)
