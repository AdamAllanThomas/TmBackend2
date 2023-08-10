# Generated by Django 4.2.4 on 2023-08-07 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='TODO', max_length=20),
        ),
    ]