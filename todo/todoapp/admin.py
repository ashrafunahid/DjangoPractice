from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_filter = ('text',)

admin.site.register(Todo, TodoAdmin)
