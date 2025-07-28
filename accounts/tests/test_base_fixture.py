from django.test import TestCase
from accounts.models import CalculatorUser


class TestAccountsFixture(TestCase):
    def setUp(self):
        return super().setUp()

    def make_account(
            self,
            name='Test',
            email='Test@test.com',
            password='123456',
    ):
        return CalculatorUser.objects.create_user(
            name=name,
            email=email,
            password=password
        )

    def make_account_admin(
            self,
            name='Test-super-user',
            email='Test@testsuper.com',
            password='123456',
    ):
        return CalculatorUser.objects.create_superuser(
            name=name,
            email=email,
            password=password
        )

    def make_form_data(self):
        return {
            'name': 'Test Nicholas',
            'email': 'test@gmail.com',
            'password1': '123456',
            'password2': '123456'
        }
