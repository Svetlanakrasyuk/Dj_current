# Generated by Django 5.0 on 2023-12-20 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodela',
            name='date_field_a',
            field=models.DateField(null=True),
        ),
    ]
