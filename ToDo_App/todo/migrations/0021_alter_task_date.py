# Generated by Django 4.2.7 on 2023-12-10 01:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0020_alter_task_date_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2023, 12, 10), null=True),
        ),
    ]
