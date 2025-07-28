from django.urls import reverse
from django.contrib.messages import get_messages
from calculator.models import Operation
from django.test import Client
from .test_base_fixtures import TestCalculatorFixture


class TestDeleteOperationsView(TestCalculatorFixture):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.user = self.make_account()
        self.operation = self.make_operation(user=self.user)
        self.url = reverse('calculator:delete-view')

    def test_operations_deleted_after_post(self):
        self.client.force_login(self.user)
        self.assertEqual(Operation.objects.filter(user=self.user).count(), 1)

        response = self.client.post(self.url)

        self.assertRedirects(response, reverse('calculator:calculator-view'))
        self.assertEqual(Operation.objects.filter(user=self.user).count(), 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any(
                "Histórico resetado" in str(m.message) for m in messages
            )
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.post(self.url)
        expected_url = reverse('accounts:login-view') + f'?next={self.url}'
        self.assertRedirects(response, expected_url)
