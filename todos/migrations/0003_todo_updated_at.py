# Generated by Django 4.2.5 on 2023-11-28 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_current_status_alter_todo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]