{% if cookiecutter.category != "LANGUAGE" %}
from django import forms
from django.utils.translation import gettext_lazy as _
from i18nfield.forms import I18nModelForm

from .models import {{ cookiecutter.__model_name }}Settings


class {{ cookiecutter.__model_name }}SettingsForm(I18nModelForm):

    def __init__(self, *args, event=None, **kwargs):
        self.instance, _ = {{ cookiecutter.__model_name }}Settings.objects.get_or_create(event=event)
        super().__init__(*args, **kwargs, instance=self.instance, locales=event.locales)

    class Meta:
        model = {{ cookiecutter.__model_name }}Settings
        fields = ("some_setting", )
        widgets = {}
{% endif %}
