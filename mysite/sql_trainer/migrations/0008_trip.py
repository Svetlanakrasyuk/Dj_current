# Generated by Django 5.0 on 2023-12-28 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_trainer', '0007_remove_book_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=25)),
                ('per_diem', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_first', models.DateField()),
                ('date_last', models.DateField()),
            ],
        ),
    ]
