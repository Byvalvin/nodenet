# Generated by Django 4.2.6 on 2023-11-13 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('likes', '0001_initial'),
        ('comments', '0004_alter_comment_post'),
        ('authors', '0020_alter_author_displayname'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_posts', '0026_alter_apppost_comment_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Owner', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(blank=True, to='comments.comment')),
                ('friend_requests', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, to='likes.like')),
                ('posts', models.ManyToManyField(blank=True, to='app_posts.apppost')),
            ],
        ),
    ]