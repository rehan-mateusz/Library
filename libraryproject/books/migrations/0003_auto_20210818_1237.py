# Generated by Django 3.2.3 on 2021-08-18 12:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210818_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_10',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn_13',
            field=models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(13)]),
        ),
    ]
