# Generated by Django 3.2.3 on 2021-08-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_isbn_13'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'author', 'published_date', 'isbn_13', 'pages', 'cover_link', 'publication_language'), name='unique_joining'),
        ),
    ]
