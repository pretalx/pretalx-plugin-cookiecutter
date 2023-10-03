from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "{{cookiecutter.module_name}}"
    verbose_name = "{{cookiecutter.human_name}}"

    class PretalxPluginMeta:
        name = gettext_lazy("{{cookiecutter.human_name}}")
        author = "{{cookiecutter.author_name}}"
        description = gettext_lazy("{{cookiecutter.short_description}}")
        visible = True
        version = __version__
        category = "{{cookiecutter.category}}"

    def ready(self):
        from . import signals  # NOQA
