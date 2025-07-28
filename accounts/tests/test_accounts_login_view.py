from .test_base_fixture import TestAccountsFixture
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class CalculatorLoginViewTest(TestAccountsFixture):
    def setUp(self):
        super().setUp()
        self.login_url = reverse('accounts:login-view')
        self.account = self.make_account()
        self.credentials = {
            'username': self.account.email,
            'password': '123456'
        }

    def test_account_login_with_valid_credentials_redirects_successfully(self):
        response = self.client.post(self.login_url, self.credentials)

        success_url = reverse('calculator:calculator-view')
        self.assertRedirects(response, success_url)

    def test_account_login_with_invalid_credentials_shows_error(self):
        invalid_credentials = {
            'username': 'invalid@test.com',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.login_url, invalid_credentials)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_account_login_authenticated_user_is_redirected(self):
        login_successful = self.client.login(**self.credentials)
        self.assertTrue(login_successful)

        response = self.client.get(self.login_url)

        success_url = reverse('calculator:calculator-view')
        self.assertRedirects(response, success_url)
