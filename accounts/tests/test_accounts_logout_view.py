from .test_base_fixture import TestAccountsFixture
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class CalculatorLogoutViewTest(TestAccountsFixture):
    def setUp(self):
        super().setUp()
        self.logout_url = reverse('accounts:logout-view')
        self.account = self.make_account()
        self.credentials = {
            'username': self.account.email,
            'password': '123456'
        }

    def test_logout_redirects_to_login_page(self):
        self.client.login(**self.credentials)
        response = self.client.post(self.logout_url)
        print(response)

        login_url = reverse('accounts:login-view')
        self.assertRedirects(response, login_url)

        response = self.client.post(reverse('calculator:calculator-view'))
        self.assertNotEqual(response.status_code, 200)

    def test_logout_requires_authentication(self):
        response = self.client.get(self.logout_url)

        self.assertNotEqual(response.status_code, 200)

    def test_logout_clears_session(self):
        self.client.login(**self.credentials)
        session = self.client.session
        session['test_key'] = 'test_value'
        session.save()

        self.client.post(self.logout_url)

        self.assertNotIn('test_key', self.client.session)
        self.assertNotIn('_auth_user_id', self.client.session)
