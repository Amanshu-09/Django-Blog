from django import forms
from .models import *
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = ('title', 'category', 'author', 'body',)

       widgets = {
           'title' : forms.TextInput(attrs={'class':'form-control'}),
           'author' : forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'author', 'type':'hidden'}),
           'category' : forms.TextInput(attrs={'class':'form-control'}),
           'body' : RichTextField(),
       }

class EditForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = ('title', 'category', 'body')

       widgets = {
           'title' : forms.TextInput(attrs={'class':'form-control'}),
           'category' : forms.TextInput(attrs={'class':'form-control'}),
           'body' : RichTextField(),
       }