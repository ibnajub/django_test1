# Generated by Django 4.1.5 on 2023-02-01 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_artc_article_artc_user_artc_likes_artc_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artc_comment',
            name='parrent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.artc_comment'),
        ),
    ]