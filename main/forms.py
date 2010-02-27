from django.forms import ModelForm
from recipes.main.models import Recipe


class RecipeForm(ModelForm):
    
    class Meta:
        model = Recipe
        fields = ['name', 'author', 'min_time', 'max_time', 'ingredients',
                  'instructions', 'categories']
