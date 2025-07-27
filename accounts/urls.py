from django.urls import path
from accounts.views import CustomLoginView, SignUpView, LogOutView


app_name = 'accounts'


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login-view'),
    path('signup/', SignUpView.as_view(), name='signup-view'),
    path('logout/', LogOutView.as_view(), name='logout-view'),
]
