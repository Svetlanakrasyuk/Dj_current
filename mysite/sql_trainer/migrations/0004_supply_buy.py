# Generated by Django 5.0 on 2023-12-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_trainer', '0003_supply'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='buy',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
