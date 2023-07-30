from django.contrib import admin
from core.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'due_date', 'completed', 'date_added')

admin.site.register(Todo, TodoAdmin)

# Register your models here.
