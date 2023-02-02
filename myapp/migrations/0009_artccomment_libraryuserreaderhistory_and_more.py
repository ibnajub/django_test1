# Generated by Django 4.1.5 on 2023-02-02 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_artc_comment_parrent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtcComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('comment_text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryUserReaderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('reading', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Artc_likes',
            new_name='ArtcLikes',
        ),
        migrations.RenameModel(
            old_name='Catalog_author',
            new_name='CatalogAuthor',
        ),
        migrations.RenameModel(
            old_name='Catalog_book',
            new_name='CatalogBook',
        ),
        migrations.RenameModel(
            old_name='Library_allowed_book',
            new_name='LibraryAllowedBook',
        ),
        migrations.RenameModel(
            old_name='Library_User_reader',
            new_name='LibraryAuthor',
        ),
        migrations.RemoveField(
            model_name='library_user_reader_history',
            name='book',
        ),
        migrations.RemoveField(
            model_name='library_user_reader_history',
            name='user',
        ),
        migrations.RenameModel(
            old_name='Artc_article',
            new_name='ArtcArticle',
        ),
        migrations.RenameModel(
            old_name='Artc_user',
            new_name='ArtcUser',
        ),
        migrations.RenameModel(
            old_name='Library_book',
            new_name='LibraryBook',
        ),
        migrations.RenameModel(
            old_name='Library_author',
            new_name='LibraryUserReader',
        ),
        migrations.DeleteModel(
            name='Artc_comment',
        ),
        migrations.DeleteModel(
            name='Library_user_reader_history',
        ),
        migrations.AddField(
            model_name='libraryuserreaderhistory',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.librarybook'),
        ),
        migrations.AddField(
            model_name='libraryuserreaderhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.libraryuserreader'),
        ),
        migrations.AddField(
            model_name='artccomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artcarticle'),
        ),
        migrations.AddField(
            model_name='artccomment',
            name='parrent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.artccomment'),
        ),
        migrations.AddField(
            model_name='artccomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artcuser'),
        ),
    ]
