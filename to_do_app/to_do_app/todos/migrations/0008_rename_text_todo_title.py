# Generated by Django 3.2.3 on 2021-06-14 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_todo_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='title',
        ),
    ]