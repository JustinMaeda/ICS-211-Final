from django.contrib import admin
from .models import Task, Project, Profile


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'due_date', 'description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_by', 'due_date')
    ordering = ('due_date',)
    date_hierarchy = 'due_date'


# Register the Task model
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assigned_to', 'status', 'due_date', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'assigned_to', 'project')
    ordering = ('due_date',)
    date_hierarchy = 'due_date'


# Register models with the admin site
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Profile)