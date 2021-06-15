from django.shortcuts import render

# Create your views here.
from to_do_app.forms_workshop.forms import UserForm


def post_request_type(request):
    form = UserForm(request.POST)

    if form.is_valid():
        fields = ['name', 'age', 'email', 'password', 'text']
        [print(field, form.cleaned_data[field]) for field in fields]
    else:
        print(form.errors)

def get_request_type(request):
    context = {
        'form': UserForm(),
    }
    return render(request, 'forms_workshop/form.html', context)


def request_type_post_or_get(request):
    if request.method == 'POST':
        return post_request_type(request)
    else:
        return get_request_type(request)
