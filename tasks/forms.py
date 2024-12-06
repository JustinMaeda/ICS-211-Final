from django import forms
from .models import Project, Profile, Task, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio',]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'due_date']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to', 'status', 'project']

    assigned_to = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only need the content for a comment