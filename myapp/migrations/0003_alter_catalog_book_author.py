# Generated by Django 4.1.5 on 2023-02-01 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_catalog_author_catalog_book_delete_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog_book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_book', to='myapp.catalog_author'),
        ),
    ]
