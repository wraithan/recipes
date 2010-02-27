from django.conf.urls.defaults import *

urlpatterns = patterns('recipes.main.views'
    (r'^$', 'recipe_index', name='recipe-index'),
    (r'^add/$', 'recipe_add', name='recipe-add'),
    (r'^view/(?P<recipe_id>\d+/'), 'recipe_view', name='recipe-view'),
)
