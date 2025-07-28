from django.views.generic import RedirectView
from django.urls import reverse_lazy


class CalculatorRedirectView(RedirectView):
    url = reverse_lazy('calculator:calculator-view')
