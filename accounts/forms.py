from django import forms
from . models import Profile
from django.contrib.auth.models import User


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('qualification', 'occupation', 'phone', 'about', 'gender', 'picture', 'state', 'senatorial_district', 'local_government', 'district', 'ward', 'street', 'house_no')