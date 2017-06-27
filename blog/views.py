i# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


import xdrlib, sys, time
reload(sys)
sys.setdefaultencoding("utf-8")

import xlrd
import json
import urllib
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import *


from haystack.forms import SearchForm, FacetedSearchForm, ModelSearchForm


from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from models import *
from forms import *
import logging, os


from django.conf import settings
from django.http import HttpResponseRedirect, QueryDict
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.shortcuts import resolve_url

# Avoid shadowing the login() and logout() views below.

from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login,
    logout as auth_logout, get_user_model, update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site



import socket, threading, time

def get_current_time():
    ISOTIMEFORMAT='%Y-%m-%d %X'
    return time.strftime(ISOTIMEFORMAT, time.localtime())[:10]


def home(request, category, load_all=True, form_class=ModelSearchForm, searchqueryset=None, ):
    current_time = get_current_time()
    form = form_class(searchqueryset=searchqueryset, load_all=load_all)
    if category:
        if category == "最新":
            result = Article.objects.all().order_by('-publish_time')
        elif category == "最热":
            result = Article.objects.all().order_by('-browse')
        # elif category == "我来提问":

        #

        elif category == "等你回答":
            result = Question.objects.all().order_by('-question_time')
    else:
        result = Article.objects.all().order_by('-publish_time')
    return render(request, 'show/home.html', {"result": result, 'current_time': current_time, "form":form, "category":category, })
