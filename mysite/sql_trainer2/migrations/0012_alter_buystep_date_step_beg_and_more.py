# Generated by Django 5.0 on 2024-01-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_trainer2', '0011_buystep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buystep',
            name='date_step_beg',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buystep',
            name='date_step_end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
