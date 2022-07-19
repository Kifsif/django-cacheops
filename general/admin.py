from django.contrib import admin
from .models import General
from django.conf import settings
from django.apps import apps


@admin.action(description='Warm cache up')
def warm_up(modeladmin, request, queryset):
    MODELS_AND_APPS = {
        "Poll": "polls",
        "Question": "polls",
        "Choice": "polls",
    }

    for model_name in MODELS_AND_APPS:
        current_model = apps.get_model(app_label=MODELS_AND_APPS[model_name], model_name=model_name)
        all_instances = current_model.objects.all()
        list(all_instances)  # The very warming the cache up.


class GeneralAdmin(admin.ModelAdmin):
    actions = [warm_up]


admin.site.register(General, GeneralAdmin)
