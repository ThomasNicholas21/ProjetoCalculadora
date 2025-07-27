from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('accounts:signup-view')

        messages.error(request, 'Login Inválido')

    context = {
        'form': form
    }
    return render(
        request,
        'accounts/pages/auth.html',
        context
    )
