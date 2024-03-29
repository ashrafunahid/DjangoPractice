from django.forms import ModelForm
from .models import QuestionModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class addQuestionForm(ModelForm):
    class Meta:
        model = QuestionModel
        fields = "__all__"
