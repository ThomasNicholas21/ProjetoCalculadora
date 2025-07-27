from django.contrib.auth.views import LogoutView


class LogOutView(LogoutView):
    next_page = '/login/'
