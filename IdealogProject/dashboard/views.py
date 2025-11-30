from django.shortcuts import render
from ideas.models import Idea
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from ideas.models import CollaborationRequest


def is_staff(user):
    return user.is_active and user.is_staff

def home(request):
    ideas = Idea.objects.filter(status='approved')
    return render(request, 'dashboard/home.html', {'ideas': ideas})


@user_passes_test(is_staff)
def admin_panel(request):
    User = get_user_model()
    ideas = Idea.objects.all().order_by('-created_at')
    users = User.objects.all().order_by('username')
    collab_requests = CollaborationRequest.objects.select_related('idea', 'requester').order_by('-created_at')
    return render(request, 'dashboard/admin_panel.html', {
        'ideas': ideas,
        'users': users,
        'collab_requests': collab_requests,
    })
