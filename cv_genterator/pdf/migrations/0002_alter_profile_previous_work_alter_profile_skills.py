# Generated by Django 5.0.6 on 2024-05-27 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='previous_work',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(max_length=2000),
        ),
    ]
