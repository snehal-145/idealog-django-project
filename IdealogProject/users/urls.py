from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # registration view: use the new `register_view` which validates and redirects to login
    path('register/', views.register_view, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    # use our explicit logout view to ensure consistent behavior
    path('logout/', views.logout_view, name="logout"),
]
