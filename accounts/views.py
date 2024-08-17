from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


class UserRegistrationView(FormView):
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("register")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLogin(LoginView):
    template_name = "user_login.html"

    def get_success_url(self):
        return reverse_lazy("home_page")


class UserLogout(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy("home_page")


class UserBankAccountUpdateView(View):
    template_name = "profile.html"

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            # form.save()
            return redirect("profile")
        return render(request, self.template_name, {"form": form})


@login_required(login_url="login")
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("change_password")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {"form": form})
