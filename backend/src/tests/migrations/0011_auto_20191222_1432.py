# Generated by Django 2.1.7 on 2019-12-22 11:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0010_auto_20191212_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Question'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 22, 14, 32, 54, 362717)),
        ),
    ]
