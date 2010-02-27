from django.conf.urls.defaults import *

urlpatterns = patterns('recipes.main.views',
    url(r'^$', 'recipe_index', name='recipe-index'),
    url(r'^add/$', 'recipe_add', name='recipe-add'),
    url(r'^view/(?P<recipe_id>\d+)/', 'recipe_view', name='recipe-view'),
)
