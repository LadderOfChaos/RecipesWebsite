
from django.shortcuts import render

from RecepiesSite.Models.email_sub import Signup
from RecepiesSite.Models.recipe import Recipe
from RecepiesSite.forms.email_sub_form import EmailSignupForm


def index(request):
    e_form = EmailSignupForm()
    if request.method == "POST":
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    Worldwide = ['Worldwide', 'Asian', 'Thai', 'Chinese', 'Indian', 'Italian']
    context = {
        'e_form': e_form,
        'recipe': Recipe.objects.order_by("-id")[:4],
        'recipe_date': Recipe.objects.order_by("-date")[:4],
        'bg_recipe': Recipe.objects.filter(type='Bulgarian').order_by('-type')[:4],
        'world_recipe': Recipe.objects.filter(type='Worldwide').order_by('-type')[:4]
    }
    return render(request, 'index.html', context)





