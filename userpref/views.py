from django.shortcuts import render
from django.db import models
from django import forms
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Userpref


def edit(request):
    form_list = []
    all_models=models.get_models(include_auto_created=False)
    if request.method == "POST":
        for current_model in all_models:
            if issubclass(current_model, Userpref) and current_model.__module__ != "userpref.admin":
                user_settings, created=current_model.objects.get_or_create(user=request.user)
                SettingsForm = _get_object_form(current_model)
                f = SettingsForm(request.POST, instance=user_settings)
                f.section_name = current_model._meta.verbose_name
                print f.section_name
                form_list.append(f)
        for current_form in form_list:
            if not current_form.is_valid():
                return render(request, "userpref_edit.html", {'form_list': form_list})
        for current_form in form_list:
            current_form.save()
        return HttpResponseRedirect(reverse('userpref_view'))
    else:
        for current_model in all_models:
            if issubclass(current_model, Userpref) and current_model.__module__ != "userpref.admin":
                user_settings, created=current_model.objects.get_or_create(user=request.user)
                SettingsForm = _get_object_form(current_model)
                f = SettingsForm(instance=user_settings)
                f.section_name = current_model._meta.verbose_name
                form_list.append(f)

    return render(request, "userpref_edit.html", {'form_list': form_list})

def view(request):
    all_models=models.get_models(include_auto_created=False)
    settings_dict={}
    for current_model in all_models:
        if issubclass(current_model, Userpref) and current_model.__module__ != "userpref.admin":
            user_settings, created=current_model.objects.get_or_create(user=request.user)
            model_dict=model_to_dict(user_settings)
            # Remove modelspecific stuff that should not be displayed
            del model_dict['id']
            del model_dict['user']
            settings_dict[current_model._meta.verbose_name] = model_dict
    return render(request, "userpref_show.html", {'user_settings': settings_dict})


def _get_object_form(m):
    class _ObjectForm(forms.ModelForm):
        class Meta:
            model = m
            exclude = ('user', )
    return _ObjectForm