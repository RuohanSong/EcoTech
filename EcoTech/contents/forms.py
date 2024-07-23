from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'document', 'link']

class ArticleSearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=False)
    author = forms.CharField(max_length=100, required=False)
    created_at = forms.DateField(required=False)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        label="Add a comment",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment...'})
    )
    class Meta:
        model = Comment
        fields = ['content']
