from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from recipes.main.forms import RecipeForm, IngredientFormSet, CategoryFormSet


def recipe_index(request):
    return render_to_response('main/recipe_index.html', {'title': "nyi"},
                              context_instance=RequestContext(request))

def recipe_view(request):
    return render_to_response('main/recipe_view.html', {'title': "nyi"},
                              context_instance=RequestContext(request))

@login_required
def recipe_add(request):
    if request.method == 'POST':
        ingredient_formset = IngredientFormSet(request.POST,
                                              prefix="ingredient")
        category_formset = CategoryFormSet(request.POST, prefix="category")
        recipe_form = RecipeForm(request.POST)

        ingredients_valid = ingredient_formset.is_valid()
        category_valid = category_formset.is_valid()
        recipe_valid = recipe_form.is_valid()

        if ingredients_valid and category_valid and recipe_valid:
            ingredient_object_list = ingredient_formset.save()

            category_object_list = category_formset.save()
        
            recipe_object = recipe_form.save(commit=False)
            recipe_object.user = request.user
            recipe_object.ingredients = ingredient_object_list
            recipe_object.category = category_object_list
            recipe_object.save()
            return HttpResponseRedirect(reverse('recipe-view'))
    else:
        ingredient_formset = IngredientFormSet(prefix="ingredients")
        category_formset = CategoryFormSet(prefix="category")
        recipe_form = RecipeForm()
    return render_to_response('main/recipe_add.html',
                              {'ingredient_formset':ingredient_formset,
                               'category_formset':category_formset,
                               'recipe_form':recipe_form,},
                              context_instance=RequestContext(request))
