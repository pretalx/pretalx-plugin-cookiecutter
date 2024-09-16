{% if cookiecutter.category != "LANGUAGE" %}
from django.urls import re_path

from pretalx.event.models.event import SLUG_REGEX

from .views import {{ cookiecutter.__model_name }}SettingsView

urlpatterns = [
    re_path(
        rf"^orga/event/(?P<event>{SLUG_REGEX})/settings/p/{{ cookiecutter.module_name }}/$",
        {{ cookiecutter.__model_name }}SettingsView.as_view(),
        name="settings",
    ),
]
{% endif %}
