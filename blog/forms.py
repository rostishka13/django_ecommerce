from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "body")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input Title'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'ident','type':'hidden'}),

            'author': forms.Select(attrs={'class': 'form-control','placeholder': 'Input author'}),
            #'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Input some text'}),
            #'title_tag': forms.TextInput(attrs={'class': 'form-control'}),

        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'update Title'}),
            #'author': forms.Select(attrs={'class': 'form-control','placeholder': 'Input author'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'update body text'}),
            #'title_tag': forms.TextInput(attrs={'class': 'form-control'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input name'}),
            #'email': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Input your email'}),

            #'author': forms.Select(attrs={'class': 'form-control','placeholder': 'Input author'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Input your comment'}),

        }