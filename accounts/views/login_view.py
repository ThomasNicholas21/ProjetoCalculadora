from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'accounts/pages/auth.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('calculator:calculator-view')

    def form_valid(self, form):
        messages.success(self.request, 'Logado com sucesso!')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Login inválido')

        return super().form_invalid(form)
