from django.urls import path
from accounts.views import (
    CalculatorLoginView,
    CalculatorSignUpView,
    CalculatorLogOutView
)


app_name = 'accounts'


urlpatterns = [
    path('login/', CalculatorLoginView.as_view(), name='login-view'),
    path('signup/', CalculatorSignUpView.as_view(), name='signup-view'),
    path('logout/', CalculatorLogOutView.as_view(), name='logout-view'),
]
