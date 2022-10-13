
from django.shortcuts import render, HttpResponseRedirect

from .models import  Messages, Recipe, Category
from .forms import MessagesForm


def index(request):
    recipes = Recipe.objects.all()
    category = Category.objects.all()

    return render(request, 'index.html', {'recipes': recipes, 'category': category})

def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    category = Category.objects.all()
    recipe_mes = recipe.messages_set.all()

    return render(request, 'recipe.html', {'recipe': recipe, 'category': category, 'recipe_mes':recipe_mes})


def category(request, id):
    category = Category.objects.all()
    categor = Category.objects.get(id=id)
    categor1 = categor.recipe_set.all()

    return render(request, 'category.html', {'categor': categor, 'categor1': categor1, 'category': category})

def messages(request, id):
    recipes = Recipe.objects.all()
    category = Category.objects.all()
    recipe = Recipe.objects.get(id=id)
    recipe_mes = recipe.messages_set.all()
    if request.method=="POST":
        message_form = MessagesForm(request.POST)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.recipe = recipe
            new_message.save()
            return render(request, 'index.html', {'recipes': recipes, 'category': category})
        return render(request, 'messages.html', {'message_form': message_form , 'recipe_mes':recipe_mes})
    message_form = MessagesForm()
    return render(request, 'messages.html', {'message_form': message_form, 'recipes': recipes, 'category': category, 'recipe':recipe})