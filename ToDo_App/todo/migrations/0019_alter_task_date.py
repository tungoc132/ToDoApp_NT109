# Generated by Django 4.2.7 on 2023-12-09 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date(2023, 12, 9), null=True),
        ),
    ]