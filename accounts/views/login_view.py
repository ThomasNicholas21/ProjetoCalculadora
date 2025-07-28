from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


class CalculatorLoginView(LoginView):
    template_name = 'accounts/pages/auth.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('calculator:calculator-view')

    def get_context_data(self, **kwargs) -> dict:
        context: dict = super().get_context_data(**kwargs)
        context['title'] = 'Tela de Login'

        return context

    def form_valid(self, form: AuthenticationForm):
        messages.success(self.request, 'Logado com sucesso!')

        return super().form_valid(form)

    def form_invalid(self, form: AuthenticationForm):
        messages.error(self.request, 'Login inválido')

        return super().form_invalid(form)

    def get_success_url(self):
        return self.success_url
