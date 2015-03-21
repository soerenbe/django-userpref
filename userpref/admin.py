from django.contrib import admin
from django.db import models
from models import Userpref
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


inline_models = ()
# fetch all models
x = models.get_models(include_auto_created=False)

# Add all found Userpref models as a inline model to the admin interface
for i in x:
    if issubclass(i, Userpref) and i.__module__ != "userpref.admin":
        class SettingsInline(admin.StackedInline):
            model = i
        inline_models += (SettingsInline,)


# Create a proxy entry for the user
class ProxyUser(User):
    class Meta:
        proxy = True
        verbose_name = User._meta.verbose_name + " " +_('Settings')
        verbose_name_plural = User._meta.verbose_name_plural + " " + _('Settings')
        # Place the proxy user at the auth section



class UserprefAdmin(admin.ModelAdmin):
    # This field will be displayed in addition to the settings fields
    _displayed_user_fields = ['username']
    inlines = inline_models
    # do not display user related fields
    exclude = [i for i in ProxyUser._meta.get_all_field_names() if i not in _displayed_user_fields]
    search_fields = ['username']

    # mark all the user fields as read only
    def get_readonly_fields(self, request, obj=None):
        return UserprefAdmin._displayed_user_fields

admin.site.register(ProxyUser, UserprefAdmin)