from django.urls import path
from . import views

# application namespace for reversing with 'ideas:...'
app_name = 'ideas'

urlpatterns = [
    # mirror a commonly used 'index' name for templates that reverse 'ideas:index'
    path('index/', views.index, name='index'),
    path('', views.idea_list, name='idea_list'),
    path('requests/', views.collab_requests_list, name='collab_requests'),
    path('requests/<int:request_id>/<str:action>/', views.collab_request_action, name='collab_request_action'),
    path('create/', views.idea_create, name='idea_create'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('<int:pk>/request-collaborate/', views.request_collaborate, name='request_collaborate'),
    path('<int:pk>/edit/', views.idea_update, name='idea_update'),
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('submit/', views.submit_idea, name='submit_idea'),
]
