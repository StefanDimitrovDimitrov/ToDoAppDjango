from django.contrib import admin

from to_do_app.todos.models import Todo
from to_do_app.todos.models.todo import Person, Category


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    sortable_by = ['text']
    list_filter = ['owner']

    # def has_change_permission(self, request, obj=None):
    #     return False # the edit is disable


admin.site.register(Todo)
admin.site.register(Person)
admin.site.register(Category)
