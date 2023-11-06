{% if cookiecutter.category != "LANGUAGE" %}
from django.urls import re_path
from pretalx.event.models.event import SLUG_REGEX

from .views import {{ cookiecutter.__model_name }}Settings

urlpatterns = [
    re_path(
        rf"^orga/event/(?P<event>{SLUG_REGEX})/settings/p/{{ cookiecutter.module_name }}/$",
        {{ cookiecutter.__model_name }}Settings.as_view(),
        name="settings",
    ),
]
urlpatterns += router.urls
{% endif %}
