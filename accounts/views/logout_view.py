from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class CalculatorLogOutView(LogoutView):
    next_page = reverse_lazy('accounts:login-view')
