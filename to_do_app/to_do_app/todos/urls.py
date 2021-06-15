from django.urls import path

from to_do_app.todos.views import index, create_todo, update_todo, delete_todo

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_todo, name='create_todo'),
    path('edit/<int:pk>', update_todo, name='edit_todo'),
    path('delete/<int:pk>', delete_todo, name='delete_todo')
]