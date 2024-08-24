from django.contrib import admin
from .models import LogModel


@admin.register(LogModel)
class PersonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LogModel._meta.get_fields() if field.name != 'id']
    list_filter = ['http_method', 'code_answer']
    search_fields = ['http_method', 'code_answer', 'ip_adress', 'data']
