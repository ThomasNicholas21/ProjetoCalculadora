from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from accounts.forms import SignUpForm


class CalculatorSignUpView(FormView):
    template_name = 'accounts/pages/auth.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login-view')

    def get_context_data(self, **kwargs) -> dict:
        context: dict = super().get_context_data(**kwargs)
        context['title'] = 'Tela de Cadastro'

        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Cadastro realizado com sucesso!')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar. Verifique os dados.')

        return super().form_invalid(form)
