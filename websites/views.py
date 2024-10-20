# Standard library imports
import os
import datetime
import json
import time
import ast

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import dateparse, timezone, translation
from django.core.exceptions import PermissionDenied
from django.contrib.admin.models import LogEntry
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import get_language, activate
from django.utils.translation import gettext as _

def set_language(request):
    next_url = request.POST.get('next', request.GET.get('next'))
    if not next_url or not url_has_allowed_host_and_scheme(url=next_url, allowed_hosts={request.get_host()}):
        next_url = request.META.get('HTTP_REFERER', '/')

    response = redirect(next_url)
    lang_code = request.POST.get('language', request.GET.get('language'))
    if lang_code and lang_code in dict(settings.LANGUAGES).keys():
        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        activate(lang_code)  # Activate the language immediately for the current request

    # Debugging output
    print(f"Session language: {request.session.get('django_language')}")
    print(f"Cookie language: {request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)}")
    print(f"Current language: {get_language()}")

    return response



# Create your views here.
def index_view(request):
    return render(request, 'site_templates/multihome.html')

def masonry_view(request):
    return render(request, 'site_templates/masonry.html')

def grid_view(request):
    return render(request, 'site_templates/grid.html')

def about_view(request):
    return render(request, 'site_templates/about.html')

def blog_view(request):
    return render(request, 'site_templates/blog.html')

def single_post_view(request):
    return render(request, 'site_templates/single-post.html')

def innovation_view(request):
    return render(request, 'site_templates/innovation.html')

def whyturkey_view(request):
    return render(request, 'site_templates/whyturkey.html')

def whybeyond_view(request):
    return render(request, 'site_templates/whybeyond.html')

def dentaslan_view(request):
    return render(request, 'site_templates/dentaslan.html')

def HT_view(request):
    return render(request, 'site_templates/HT.html')

def estetik_view(request):
    return render(request, 'site_templates/estetik.html')

def comingsoon_view(request):
    return render(request, 'site_templates/comingsoon.html')

def dashboard_view(request):
    return render(request, 'site_templates/dashboard.html')

def dentaslanFR_view(request):
    return render(request, 'site_templates/dentaslanFR.html')


def tooth_model_view(request):
    return render(request, 'site_templates/tooth_viewer.html')