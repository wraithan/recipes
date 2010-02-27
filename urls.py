from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template':'index.html'}),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^accounts/profile/$', direct_to_template, {
            'template': 'profile.html'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^recipe/', include('recipes.main.urls')),
    (r'^todo/', direct_to_template, {'template':'todo/master.html'}),
)
