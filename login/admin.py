from django.contrib import admin
from django.apps import apps
from .models import *

# Automatically register all models in the current app
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass  # Skip models that are already registered
