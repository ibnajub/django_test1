# Generated by Django 4.1.5 on 2023-02-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_artc_comment_parrent'),
    ]

    operations = [
        migrations.AddField(
            model_name='artc_comment',
            name='parrent_level',
            field=models.IntegerField(default=0),
        ),
    ]
