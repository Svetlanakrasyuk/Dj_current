# Generated by Django 5.0 on 2024-01-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_trainer2', '0004_alter_book_author_alter_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=30)),
                ('days_delivery', models.IntegerField()),
            ],
        ),
    ]
