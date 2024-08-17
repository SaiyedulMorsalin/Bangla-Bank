from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
    path(
        "logout/confirmation/",
        TemplateView.as_view(template_name="logout_conf.html"),
        name="logout_conf",
    ),
    path("profile/", views.UserBankAccountUpdateView.as_view(), name="profile"),
    path(
        "user/profile/password/change/",
        views.change_password,
        name="password_change",
    ),
]
