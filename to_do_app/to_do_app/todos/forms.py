from django import forms
from django.core.exceptions import ValidationError


def validate_dot(value):
    if '.' in value:
        raise forms.ValidationError('\'.\' is present in value')


def validate_bot_catcher_empty(value):
    if value:
        raise ValidationError('You are a bot')


class CreateTodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        # validators=[
        #     validate_dot,
        #     # validate_bot_catcher_empty,
        # ],

    )
    state = forms.BooleanField()
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-text-area',
                'rows': 1,
            },
        ),
    )

    # bot_catcher = forms.CharField(
    #     widget=forms.HiddenInput(),
    # )
    #
    # def clean_bots_catcher(self):
    #     value = self.cleaned_data['bots_catcher']
    #     validate_bot_catcher_empty(value)


class UpdateTodoForm(CreateTodoForm):
    state = forms.BooleanField()