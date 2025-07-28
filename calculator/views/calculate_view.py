from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from calculator.models import Operation
from utils.expression.calculate_expression import Calc


class CalculatorView(LoginRequiredMixin, TemplateView):
    template_name = 'calculator/pages/calculator.html'
    login_url = 'accounts:login-view'

    def get_context_data(self, **kwargs) -> dict[int | float | Operation]:
        context: dict = super().get_context_data(**kwargs)
        operations: Operation = Operation.objects.filter(
            user=self.request.user
        ).order_by('-id')

        context['result'] = 0
        context['operations'] = operations
        context['title'] = 'Calculadora'

        return context

    def post(self, request, *args, **kwargs):
        expression: str = request.POST.get('expression')
        context: dict = self.get_context_data()
        result: int | float = 0

        try:
            result = Calc.evaluate(expression)

        except ZeroDivisionError:
            messages.error(request, 'Erro de divisão por zero!')

        except SyntaxError:
            messages.error(request, 'Erro de sintaxe!')

        except Exception:
            messages.error(request, 'Erro ao avaliar a expressão!')

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        Operation.objects.create(
            user=request.user,
            parameters=str(expression),
            result=str(result)
        )

        context.update(
            {
                'result': result
            }
        )
        return self.render_to_response(context)
