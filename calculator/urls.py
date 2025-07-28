from django.urls import path
from calculator.views import (
    CalculatorView,
    DeleteOperationsView,
    CalculatorRedirectView
)


app_name = 'calculator'


urlpatterns = [
    path(
        '',
        CalculatorRedirectView.as_view(),
        name='redirect-view'
    ),
    path(
        'calculator/',
        CalculatorView.as_view(),
        name='calculator-view'
    ),
    path(
        'delete_operations/',
        DeleteOperationsView.as_view(),
        name='delete-view'
    ),
]
