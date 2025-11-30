from django.contrib import admin
from django.urls import path, include
from dashboard.views import home as dashboard_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('dashboard.urls')),
    # compatibility: provide a non-namespaced 'home' name for code that reverses 'home'
    path('home/', dashboard_home, name='home'),
    # provide a top-level 'index' name (some templates or redirects may reverse 'index')
    path('index/', dashboard_home, name='index'),
    path('ideas/', include('ideas.urls', namespace='ideas')),
    path('teams/', include('teams.urls')),
]
