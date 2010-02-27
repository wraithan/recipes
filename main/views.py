from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from recipes.main.forms import RecipeForm


def recipe_index(request):
    return render_to_response('main/recipe_index.html', {'title': "nyi"},
                              context_instance=RequestContext(request))

def recipe_view(request):
    return render_to_response('main/recipe_view.html', {'title': "nyi"},
                              context_instance=RequestContext(request))

@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.save()
            return HttpResponseRedirect(reverse('recipe-view'))
    else:
        form = RecipeForm()
    return render_to_response('main/recipe_add.html', {'form':form},
                              context_instance=RequestContext(request))
