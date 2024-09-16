from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView
from pretalx.common.mixins.views import PermissionRequired

{% if cookiecutter.category != "LANGUAGE" %}
from .forms import {{ cookiecutter.__model_name }}SettingsForm


class {{ cookiecutter.__model_name }}SettingsView(PermissionRequired, FormView):
    permission_required = "orga.change_settings"
    template_name = "{{ cookiecutter.module_name }}/settings.html"
    form_class = {{ cookiecutter.__model_name }}SettingsForm

    def get_success_url(self):
        return self.request.path

    def get_object(self):
        return self.request.event

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["event"] = self.request.event
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _("The {{ cookiecutter.human_name }} settings were updated."))
        return super().form_valid(form){% endif %}
