# Generated by Django 4.0 on 2022-01-10 15:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickabook', '0003_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotes',
            name='quote_title',
        ),
        migrations.AddField(
            model_name='quotes',
            name='quote_author',
            field=models.CharField(max_length=500, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AddField(
            model_name='quotes',
            name='quote_description',
            field=models.TextField(null=True),
        ),
    ]