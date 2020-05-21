from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from .views import RegisterView

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView, name='login'),
    path('logout/', auth_views.LogoutView, {"next_page":
         reverse_lazy('accounts:login')}, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
