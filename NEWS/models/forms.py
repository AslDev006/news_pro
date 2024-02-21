from django import forms
from .models import *


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "slug", "body", "publish_time", "status",  "category", "image"]



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']