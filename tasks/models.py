from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    status_choices = [('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed')]
    status = models.CharField(max_length=50, choices=status_choices, default='not_started')

    def __str__(self):
        return self.title