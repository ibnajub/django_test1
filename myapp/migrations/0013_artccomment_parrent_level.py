# Generated by Django 4.1.5 on 2023-02-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_artccomment_parrent'),
    ]

    operations = [
        migrations.AddField(
            model_name='artccomment',
            name='parrent_level',
            field=models.IntegerField(default=0),
        ),
    ]
