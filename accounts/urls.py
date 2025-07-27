from django.urls import path
from accounts.views import login, signup


app_name = 'accounts'


urlpatterns = [
    path('login/', login, name='login-view'),
    path('signup/', signup, name='signup-view'),
]
