from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CalculatorUser


@admin.register(CalculatorUser)
class CalculatorUserAdmin(UserAdmin):
    model = CalculatorUser
    list_display = ('email', 'name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('name',)}),
        ('Permissões', {'fields': ('is_admin',)}),
        ('Ativo', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_admin'),
        }),
    )
    ordering = ('email',)
    filter_horizontal = ()
