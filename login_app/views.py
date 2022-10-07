from .forms import SignupForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect


class GroupUserForPortal1Mixin(UserPassesTestMixin):
    #raise_exception = True
    def test_func(self):
        if self.request.user.id is None: # 未ログインユーザ処理
            return False
        else:
            groups = []
            query_set = Group.objects.filter(user = self.request.user)
            for g in query_set:
                groups.append(str(g))
            if 'grp_1' in groups:
                return True
            else:
                return False

class GroupUserForPortal2Mixin(UserPassesTestMixin):
    #raise_exception = True
    def test_func(self):
        if self.request.user.id is None: # 未ログインユーザ処理
            return False
        else:
            groups = []
            query_set = Group.objects.filter(user = self.request.user)
            for g in query_set:
                groups.append(str(g))
            if 'grp_2' in groups:
                return True
            else:
                return False



class MySignupView(CreateView):
    template_name = 'login_app/signup.html'
    form_class = SignupForm
    success_url = '/login_app/user/'
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result

class MyLoginView(LoginView):
    template_name = 'login_app/login.html'
    form_class = LoginForm

class MyLogoutView(LogoutView):
    template_name = 'login_app/logout.html'

class MyUserView(LoginRequiredMixin, TemplateView):
    template_name = 'login_app/user.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class MyOtherView(LoginRequiredMixin, TemplateView):
    template_name = 'login_app/other.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(username=self.request.user.username)
        return context

class Portal_1_View(GroupUserForPortal1Mixin, TemplateView):
    template_name = 'login_app/portal_1.html'

class Portal_2_View(GroupUserForPortal2Mixin, TemplateView):
    template_name = 'login_app/portal_2.html'

class Portal_View(LoginRequiredMixin, TemplateView):
    template_name = 'login_app/portal.html'

class LoginErrorView(TemplateView):
    template_name = 'login_app/403.html'

