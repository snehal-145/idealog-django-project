from django.shortcuts import render


def team_list(request):
    """Simple teams list view to prevent import errors and show teams page."""
    return render(request, 'teams/list.html')
