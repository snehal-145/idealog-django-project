from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Idea
from .forms import IdeaForm
from .models import CollaborationRequest

def home(request):
    return render(request, 'ideas/base.html') 

def index(request):
    ideas = Idea.objects.filter(status='approved')
    # render the namespaced template path
    return render(request, 'ideas/index.html', {'ideas': ideas})

@login_required
def idea_list(request):
    ideas = Idea.objects.filter(created_by=request.user)
    return render(request, 'ideas/idea_list.html', {'ideas': ideas})

@login_required
def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})


@login_required
def request_collaborate(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        message = request.POST.get('message', '').strip()
        # prevent duplicate pending requests from same user
        existing = CollaborationRequest.objects.filter(idea=idea, requester=request.user, status='pending').exists()
        if not existing:
            CollaborationRequest.objects.create(idea=idea, requester=request.user, message=message)
        return redirect('ideas:idea_detail', pk=pk)
    return render(request, 'ideas/request_collaborate.html', {'idea': idea})


@staff_member_required
def collab_requests_list(request):
    # admin view: list pending requests
    requests = CollaborationRequest.objects.filter(status='pending')
    return render(request, 'ideas/collab_requests_list.html', {'requests': requests})


@staff_member_required
def collab_request_action(request, request_id, action):
    cr = get_object_or_404(CollaborationRequest, pk=request_id)
    if action == 'approve':
        cr.status = 'approved'
        cr.idea.collaborators.add(cr.requester)
        cr.idea.save()
        cr.save()
    elif action == 'reject':
        cr.status = 'rejected'
        cr.save()
    return redirect('ideas:collab_requests')

@login_required
def idea_create(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.created_by = request.user
            idea.save()
            return redirect('ideas:idea_list')
    else:
        form = IdeaForm()
    return render(request, 'ideas/idea_form.html', {'form': form})

@login_required
def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:idea_list')
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/idea_form.html', {'form': form})

@login_required
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        idea.delete()
        return redirect('ideas:idea_list')
    return render(request, 'ideas/idea_confirm_delete.html', {'idea': idea})

def submit_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.created_by = request.user
            idea.save()
            return redirect('dashboard:home')
    else:
        form = IdeaForm()
    return render(request, 'ideas/submit_idea.html', {'form': form})
