from django.test import RequestFactory
from .test_base_fixtures import TestCalculatorFixture
from django.contrib.messages.storage.fallback import FallbackStorage
from django.urls import reverse
from django.contrib.messages import get_messages
from calculator.views import CalculatorView
from calculator.models import Operation


class CalculatorViewTest(TestCalculatorFixture):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = self.make_account()
        self.url = reverse('calculator:calculator-view')
        self.view = CalculatorView.as_view()
        return super().setUp()

    def test_post_valid_expression(self):
        request = self.factory.post(self.url, {'expression': '2 + 3 * 4'})
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = self.view(request)
        context = response.context_data

        operation = Operation.objects.filter(user=self.user).last()
        self.assertEqual(operation.parameters, '2 + 3 * 4')
        self.assertEqual(operation.result, '14')
        self.assertEqual(context['result'], 14)

        storage = get_messages(request)
        self.assertEqual(len(storage), 0)

    def test_post_division_by_zero(self):
        request = self.factory.post(self.url, {'expression': '1 / 0'})
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = self.view(request)
        context = response.context_data

        storage = get_messages(request)
        messages = list(storage)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Erro de divisão por zero!')

        self.assertEqual(context['result'], 0)

    def test_post_syntax_error(self):
        request = self.factory.post(self.url, {'expression': '2 + * 3'})
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = self.view(request)
        context = response.context_data

        storage = get_messages(request)
        messages = list(storage)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Erro de sintaxe!')
        self.assertEqual(context['result'], 0)

    def test_float_result_converted_to_int(self):
        request = self.factory.post(self.url, {'expression': '4 / 2'})
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = self.view(request)
        context = response.context_data

        self.assertEqual(context['result'], 2)
        self.assertIsInstance(context['result'], int)

        operation = Operation.objects.filter(user=self.user).last()
        self.assertEqual(operation.result, '2')
