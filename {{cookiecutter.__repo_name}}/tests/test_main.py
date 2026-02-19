{% if cookiecutter.category != "LANGUAGE" %}
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_orga_can_access_settings(orga_client, event):
    response = orga_client.get(
        reverse(
            "plugins:{{cookiecutter.module_name}}:settings",
            kwargs={"event": event.slug},
        ),
        follow=True,
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_reviewer_cannot_access_settings(review_client, event):
    response = review_client.get(
        reverse(
            "plugins:{{cookiecutter.module_name}}:settings",
            kwargs={"event": event.slug},
        ),
    )
    assert response.status_code == 404
{% else %}
def test_plugin_importable():
    import {{cookiecutter.module_name}}  # noqa: F401
{% endif %}
