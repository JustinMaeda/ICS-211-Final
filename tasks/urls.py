from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.guest_login_view, name='guest_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_task/<int:project_id>/', views.create_task, name='create_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('comment_task/<int:task_id>/', views.comment_task, name='comment_task'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]