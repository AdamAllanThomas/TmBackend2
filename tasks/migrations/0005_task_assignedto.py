# Generated by Django 4.2.4 on 2023-08-05 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_remove_task_assignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignedTo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_assigned', to=settings.AUTH_USER_MODEL),
        ),
    ]
