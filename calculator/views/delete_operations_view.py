from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from calculator.models import Operation


class DeleteOperationsView(LoginRequiredMixin, View):
    login_url = 'accounts:login-view'

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        Operation.objects.filter(user=request.user).delete()
        messages.success(request, 'Histórico resetado')

        return redirect('calculator:calculator-view')
