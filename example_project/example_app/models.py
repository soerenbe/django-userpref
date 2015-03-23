from django.db import models
from userpref.models import Userpref

class TestSettings(Userpref):
    superhero = models.BooleanField(default=True, verbose_name='I am a Superhero')
    codename = models.CharField(max_length=100, default="Superman", verbose_name='My codename')

    class Meta:
        verbose_name = "Superhero settings"
