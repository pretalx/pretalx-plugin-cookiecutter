from django.db import models


{% if cookiecutter.category == "RECORDING" %}
class {{ cookiecutter.__model_name }}Link(models.Model):
    submission = models.OneToOneField(
        to="submission.Submission",
        on_delete=models.CASCADE,
        related_name="{{ cookiecutter.module_name }}_link",
    )
    video_id = models.CharField(max_length=20)

    @property
    def player_link(self):
        return f"https://www.{{ cookiecutter.module_name }}.com/embed/{self.video_id}"

    @property
    def direct_link(self):
        return f"https://{{ cookiecutter.module_name }}/watch?v={self.video_id}"

    @property
    def iframe(self):
        return f'<div class="embed-responsive embed-responsive-16by9"><iframe src="{self.player_link}" frameborder="0" allowfullscreen></iframe></div>'


{% endif %}
{% if cookiecutter.category != "LANGUAGE" %}
class {{ cookiecutter.__model_name }}Settings(models.Model):
    event = models.OneToOneField(
        to="event.Event",
        on_delete=models.CASCADE,
        related_name="{{ cookiecutter.module_name }}_settings",
    )
    some_setting = models.CharField(max_length=10, default="A")
{% endif %}
