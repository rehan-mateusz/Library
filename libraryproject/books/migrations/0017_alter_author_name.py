# Generated by Django 3.2.3 on 2021-08-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]