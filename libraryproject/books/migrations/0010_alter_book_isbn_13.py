# Generated by Django 3.2.3 on 2021-08-19 06:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_13',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(13)]),
        ),
    ]
