# Generated by Django 2.1.7 on 2020-03-06 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0017_auto_20200306_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answerType',
        ),
        migrations.AlterField(
            model_name='testresult',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 10, 14, 39, 204380)),
        ),
    ]
