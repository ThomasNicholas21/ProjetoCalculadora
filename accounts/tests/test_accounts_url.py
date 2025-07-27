from .test_base_fixture import TestAccountsFixture
from django.urls import reverse


class TestAccountsURL(TestAccountsFixture):
    def test_accounts_login_url_is_correct(self):
        login_url = reverse('accounts:login-view')
        self.assertEqual(login_url, '/login/')

    def test_accounts_signup_url_is_correct(self):
        login_url = reverse('accounts:signup-view')
        self.assertEqual(login_url, '/signup/')
