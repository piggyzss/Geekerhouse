# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
# from django.forms import ModelForm

from django import forms
# 解决了author的问题

from django.contrib.auth.models import *
from django.contrib import admin

from django.core.urlresolvers import get_script_prefix
from django.utils.encoding import iri_to_uri, python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class vote_data(models.Model):
    voter = models.CharField(max_length=50)
    candidate = models.CharField(max_length=50)


class user_registe(models.Model):
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    # user_password = models.IntegerField(max_length=200)



class login_form(forms.Form):
    # user_name = forms.CharField(label=(u"用户名"), max_length=30, initial=u"请输入您的用户名")

    user_name = forms.CharField(label=(u"用户名"), max_length=30)
    user_password = forms.CharField(label=(u"密  码"), widget=forms.PasswordInput)
    # user_mail = forms.CharField(label=(u"邮 箱"), max_length=30,)

    # user_tele = forms.CharField(label=(u"电 话"), max_length=30,)


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.tag_name


class Classification(models.Model):
    classification_name = models.CharField(max_length=20, blank=True)
    introduction = models.TextField(blank=True)
    def __unicode__(self):
        return u'%s' % (self.classification_name)


class Author(models.Model):
    name = models.ForeignKey(User)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    def __unicode__(self):
        return u'%s' % (self.name)


# @python_2_unicode_compatible

class Article(models.Model):
    caption = models.CharField(max_length=80)
    classification = models.ForeignKey(Classification)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    introduction = models.TextField(blank=True)
    collect = models.IntegerField(default=0)
    browse = models.IntegerField(default=0)
    catalog = models.TextField(blank=True)
    # def publish(self):

    #     self.publish_time = timezone.now()

    #     self.save()

    def __unicode__(self):
        return self.caption

    class Meta:
        verbose_name=u"blog"

    # def __str__(self):

    #     return self.caption



# Create your models here.


class Question(models.Model):
    questioner = models.ForeignKey(User)
    question = models.TextField(blank=True)
    question_title = models.CharField(max_length=100)
    question_classification = models.ForeignKey(Classification)
    question_time = models.DateTimeField(auto_now_add=True)
    question_answer_num = models.IntegerField(default=0)
    browse = models.IntegerField(default=0)
    attention = models.IntegerField(default=0)
    def __unicode__(self):
        return u'%s' % (self.question)


class Answer(models.Model):
    answerer = models.ForeignKey(User)
    answer = models.TextField(blank=True)
    answer_time = models.DateTimeField(auto_now_add=True)
    answer_praise_num = models.IntegerField(default=0)
    question_title = models.CharField(max_length=100)
    def __unicode__(self):
        return u'%s' % (self.answer)

class Upload_course(models.Model):
    author = models.ForeignKey(User)
    caption = models.CharField(max_length=80)
    introduction = models.TextField(blank=True)
    classification = models.ForeignKey(Classification)
    publish_time = models.DateTimeField(auto_now_add=True)
    content = models.FileField(upload_to="media/files/")
    def __unicode__(self):
        return u'%s' % (self.content)

class Current_user_info(User):
    #signature_line = models.TextField(blank=True)

    write_blog = models.ManyToManyField(Article, blank=True)
    ask_question = models.ManyToManyField(Question, blank=True)
    answer_question = models.ManyToManyField(Answer, blank=True)
    # upload_course = models.ManyToManyField(UploadFile, blank=True)

    class Meta:
        verbose_name = "User_info"

class ExaminationType(models.Model):
    examination_type = models.CharField(max_length=20, blank=True)
    def __unicode__(self):
        return u'%s' % (self.examination_type)


class Examination_database(models.Model):
    examination_question = models.TextField()
    examination_answer = models.TextField()
    examination_type = models.ForeignKey(ExaminationType)
