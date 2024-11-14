{% if cookiecutter.category == "RECORDING" %}
from django.dispatch import receiver
from django.urls import reverse

from pretalx.agenda.signals import register_recording_provider
from pretalx.orga.signals import nav_event_settings


@receiver(register_data_exporters, dispatch_uid="exporter_{{ cookiecutter.module_name }}")
def register_data_exporter(sender, **kwargs):
    from .exporter import MyExporter
    return MyExporter


@receiver(nav_event_settings)
def {{ cookiecutter.module_name }}_settings(sender, request, **kwargs):
    if not request.user.has_perm("orga.change_settings", request.event):
        return []
    return [
        {
            "label": "{{ cookiecutter.human_name }}",
            "url": reverse(
                "plugins:{{ cookiecutter.module_name }}:settings",
                kwargs={"event": request.event.slug},
            ),
            "active": request.resolver_match.url_name
            == "plugins:{{ cookiecutter.module_name }}:settings",
        }
    ]
{% elif cookiecutter.category == "LANGUAGE" %}
from django.dispatch import receiver

from pretalx.common.signals import register_locales


@receiver(register_locales)
def register_locales(**kwargs):
    event = kwargs.pop("sender", None)
    if event:
        if "{{ cookiecutter.module_name }}" not in getattr(event, "plugin_list", None) or []:
            return []
    return ["my-lang"]
{% else %}
from django.dispatch import receiver
from django.urls import reverse

from pretalx.orga.signals import nav_event_settings


@receiver(nav_event_settings)
def {{ cookiecutter.module_name }}_settings(sender, request, **kwargs):
    if not request.user.has_perm("orga.change_settings", request.event):
        return []
    return [
        {
            "label": "{{ cookiecutter.human_name }}",
            "url": reverse(
                "plugins:{{ cookiecutter.module_name }}:settings",
                kwargs={"event": request.event.slug},
            ),
            "active": request.resolver_match.url_name
            == "plugins:{{ cookiecutter.module_name }}:settings",
        }
    ]
{% endif %}
