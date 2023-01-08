from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_filter = ('text',)
    list_display = ('text', 'user')

admin.site.register(Todo, TodoAdmin)
