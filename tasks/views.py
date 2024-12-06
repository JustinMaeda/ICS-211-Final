from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import ProjectForm, UserRegistrationForm, ProfileForm, TaskForm, CommentForm
from .models import Profile, Project, Task

@login_required
def dashboard(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'tasks/dashboard.html', {'projects': projects})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'tasks/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'tasks/login.html')


def guest_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'tasks/guest_login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'tasks/profile_view.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'tasks/edit_profile.html', {'form': form})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'tasks/create_project.html', {'form': form})


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = project.tasks.all()
    return render(request, 'tasks/project_detail.html', {'project': project, 'tasks': tasks})


@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            # Create the task
            task = form.save(commit=False)
            task.project = project  # Associate the task with the project
            task.save()
            return redirect('project_detail', project_id=project.id)  # Redirect to project detail page
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {'form': form, 'project': project})


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()

    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save the edited task
            return redirect('task_detail', task_id=task.id)  # Redirect to task detail page
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task,html', {'form': form, 'task': task})


@login_required
def comment_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task  # Associate the comment with the task
            comment.user = request.user  # Set the current user as the commenter
            comment.save()
            return redirect('task_detail', task_id=task.id)  # Redirect back to the task details page
    else:
        form = CommentForm()

    return render(request, 'tasks/comment_task.html', {'form': form, 'task': task})
