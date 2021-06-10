from django.urls import path

from to_do_app.todos.views import index

urlpatterns = [
    path('', index)
]