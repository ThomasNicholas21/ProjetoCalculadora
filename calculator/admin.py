from django.contrib import admin
from .models import Operation


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'parameters', 'result', 'created_at'
    ]
    ordering = '-id',
    list_per_page = 5
