from django import forms
from .models import *
from django.contrib import admin

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('caption', 'classification', 'introduction', 'catalog', 'content', )

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_title', 'question', 'question_classification', )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer', )

class UploadFileForm(forms.ModelForm):
    content = forms.FileField(widget=forms.FileInput(attrs={'id': 'file-4', 'type':"file", 'class':"file", 'data-upload-url':"#"}))
    class Meta:
        model = Upload_course
        # fields = ('caption', 'introduction', 'classification', 'content', )

        fields = ('content', )
        # content = forms.FileField(widget=forms.TextInput(attrs={'name': 'file_name',}))


from django import forms
from .models import *
from django.contrib import admin

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('caption', 'classification', 'introduction', 'catalog', 'content', )

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_title', 'question', 'question_classification', )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer', )

