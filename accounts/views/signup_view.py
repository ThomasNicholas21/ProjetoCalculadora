from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import SignUpForm


def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Logado com sucesso!')
            return redirect('accounts:login-view')

        messages.error(request, 'Login Inválido')

    context = {
        'form': form
    }
    return render(
        request,
        'accounts/pages/auth.html',
        context
    )
