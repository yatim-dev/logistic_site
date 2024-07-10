from .models import UserInput
from django.forms import ModelForm, TextInput


class UserInputForm(ModelForm):
    class Meta:
        model = UserInput
        fields = ["string"]
        widgets = {"string": TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите id заказа"
        })}

