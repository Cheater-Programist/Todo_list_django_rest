from django.contrib import admin
from apps.base.models import Todo 
 
# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')