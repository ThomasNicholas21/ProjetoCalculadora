from .test_base_fixture import TestAccountsFixture
from django.urls import reverse
from accounts.forms import SignUpForm
from accounts.models import CalculatorUser


class CalculatorSignUpViewTest(TestAccountsFixture):
    def setUp(self):
        self.url = reverse('accounts:signup-view')
        self.form_data = self.make_form_data()
        self.form_data['password1'] = 'test123456789'
        self.form_data['password2'] = 'test123456789'
        self.success_url = reverse('accounts:login-view')
        return super().setUp()

    def test_signup_view_returns_status_code_200_OK(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_signup_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'accounts/pages/auth.html')

    def test_signup_view_uses_signup_form(self):
        response = self.client.get(self.url)
        self.assertIsInstance(response.context['form'], SignUpForm)

    def test_signup_view_creates_user_on_success(self):
        self.assertFalse(
            CalculatorUser.objects.filter(
                email=self.form_data['email']
            ).exists()
        )
        response = self.client.post(self.url, data=self.form_data)

        self.assertTrue(
            CalculatorUser.objects.filter(
                email=self.form_data['email']
            ).exists()
        )
        self.assertRedirects(response, self.success_url)

    def test_signup_view_does_not_create_user_with_invalid_data(self):
        invalid_data = {
            'name': 'Test Invalid',
            'email': 'invalid@test.com',
            'password1': '123456',
            'password2': '654321'
        }
        response = self.client.post(self.url, data=invalid_data, follow=True)

        self.assertFalse(
            CalculatorUser.objects.filter(email=invalid_data['email']).exists()
        )
        self.assertEqual(response.status_code, 200)

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Erro ao cadastrar. Verifique os dados.'
        )

    def test_signup_view_does_not_create_user_with_duplicate_email(self):
        self.make_account(email='existing@test.com')

        duplicate_data = {
            'name': 'Duplicate User',
            'email': 'existing@test.com',
            'password1': '123456',
            'password2': '123456'
        }

        response = self.client.post(self.url, data=duplicate_data, follow=True)

        self.assertEqual(
            CalculatorUser.objects.filter(
                email=duplicate_data['email']
            ).count(),
            1
        )

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Erro ao cadastrar. Verifique os dados.'
        )
