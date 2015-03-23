Django-Userpref
===============

django-userpref provides a abstract and reuseable framework for userspecific settings

This includes:

* Abstract UserPref Class
* Admin interface
* Templates for an userspecific settings page


Basic usage
===========

Just define a abstract model that can be used in the applications.
In you app you should define something like:

.. code:: python

    from userpref.models import Userpref

    class MyappSettings(Userpref):
        special_setting = models.BooleanField(default=False, verbose_name='Make me a superhero')
        another_field = models.CharField(max_length=100, default="<unset>")

        class Meta:
            verbose_name = "My Custom Setting for app Myapp"


In your application or template you can access the settings over the users attributes

.. code:: html

    {% if request.user.myappsettings.special_settings %}
        You are special man!
    {% endif %}