from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Feedback


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'phone', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'name', 'email', 'phone', 'bio']


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['problems_text', 'likes_dislikes_text', 'feature_choice', 'feature_reason']
