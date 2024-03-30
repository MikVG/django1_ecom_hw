from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, confirm_email, generate_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm-register/<str:token>', confirm_email, name='confirm_email'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html'),
         name='password_reset'),
    path('password-generate/', generate_new_password, name='generate_new_password'),
]
