# Generated by Django 4.1.5 on 2023-01-31 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog_author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cat_book', to='myapp.catalog_author')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]