# Generated by Django 4.2.6 on 2023-11-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0033_alter_apppost_origin_alter_apppost_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apppost',
            old_name='comment_count',
            new_name='count',
        ),
        migrations.AddField(
            model_name='apppost',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]