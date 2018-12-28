from django.forms import Form, ModelForm
from django.contrib.auth.forms import UserCreationForm

from core.models import User, Car


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )


class UpdateProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ("favorite_brand", "about_me", "image")


class CarCreateForm(ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'brand', 'year', 'mileage', 'gas','image']