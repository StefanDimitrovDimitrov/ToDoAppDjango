from django.urls import path

from to_do_app.forms_workshop.views import request_type_post_or_get

urlpatterns = [
    path('', request_type_post_or_get, name='show_form_data'),
]