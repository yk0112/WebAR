from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.contrib.auth import login, authenticate
from .forms import LoginForm,registerForm


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'

# class Register(CreateView):
#     template_name = 'accounts/register.html'
#     form_class = registerForm
#     success_url = reverse_lazy('.')
#     # validator
#     def form_valid(self, form):
#         user = form.save() 
#         login(self.request, user) 
#         self.object = user 
#         return redirect(to=self.get_success_url()) 


def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../WebAR/markerbase')
    else:
        form = registerForm()
    return render(request, 'accounts/register.html', {'form': form})