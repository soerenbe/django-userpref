from django.db import models
from django.contrib.auth.models import User


"""
Just define a abstract model that can be used in the applications.
In you app you should define something like:

    from userpref.models import Userpref

    class MyappSettings(Userpref):
        special_setting = models.BooleanField(default=False)
        another_field = models.CharField(max_length=100, default="<unset>")


"""

class Userpref(models.Model):
    user = models.OneToOneField(User)

    class Meta:
        abstract = True

