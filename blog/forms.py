from django import forms
from .models import Category, Post, Tag


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'categories', 'tags', 'picture', 'description', 'previous_post', 'next_post', 'publish')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"