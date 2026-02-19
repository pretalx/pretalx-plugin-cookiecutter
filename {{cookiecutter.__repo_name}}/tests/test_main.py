{% if cookiecutter.category != "LANGUAGE" -%}
import pytest
from django.urls import reverse

from {{cookiecutter.module_name}}.models import {{cookiecutter.__model_name}}Settings

SETTINGS_URL_NAME = "plugins:{{cookiecutter.module_name}}:settings"


@pytest.mark.django_db
def test_orga_can_access_settings(orga_client, event):
    response = orga_client.get(
        reverse(SETTINGS_URL_NAME, kwargs={"event": event.slug}),
        follow=True,
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_orga_can_save_settings(orga_client, event):
    url = reverse(SETTINGS_URL_NAME, kwargs={"event": event.slug})
    response = orga_client.post(url, {"some_setting": "B"}, follow=True)
    assert response.status_code == 200
    assert {{cookiecutter.__model_name}}Settings.objects.get(event=event).some_setting == "B"


@pytest.mark.django_db
def test_reviewer_cannot_access_settings(review_client, event):
    response = review_client.get(
        reverse(SETTINGS_URL_NAME, kwargs={"event": event.slug}),
    )
    assert response.status_code == 404
{%- else -%}
def test_plugin_importable():
    import {{cookiecutter.module_name}}  # noqa: F401
{%- endif %}
