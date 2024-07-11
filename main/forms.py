from .models import UserInput, Support
from django.forms import ModelForm, TextInput, Textarea


class UserInputForm(ModelForm):
    class Meta:
        model = UserInput
        fields = ["string"]
        widgets = {"string": TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите id заказа"
        })}


class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = ["email", "order_id","title", "message"]
        widgets = {
            "email": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите вашу почту"
            }),
            "order_id": TextInput(attrs={
               "class": "form-control",
               "placeholder": "Введите id заказа"
            }),
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите заголовок сообщения"
            }),
            "message": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Введите сообщение"
            })
        }
