# Generated by Django 4.1.5 on 2023-02-01 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_library_allowed_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artc_article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('header', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artc_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Artc_likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('like_dislike', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artc_article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artc_user')),
            ],
        ),
        migrations.CreateModel(
            name='Artc_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('comment_text', models.CharField(max_length=1000)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artc_article')),
                ('parrent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.artc_comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artc_user')),
            ],
        ),
        migrations.AddField(
            model_name='artc_article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artc_user'),
        ),
    ]
