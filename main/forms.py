from django.forms import ModelForm
from django.forms.models import modelformset_factory
from recipes.main.models import Recipe, Ingredient, Category


class RecipeForm(ModelForm):
    
    class Meta:
        model = Recipe
        fields = ['name', 'author', 'min_time', 'max_time', 'instructions']

IngredientFormSet = modelformset_factory(Ingredient)
CategoryFormSet = modelformset_factory(Category)
