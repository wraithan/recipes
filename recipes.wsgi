import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'recipes.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

