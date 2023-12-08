# Generated by Django 4.2.6 on 2023-11-12 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_posts', '0021_alter_apppost_author_alter_apppost_contenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apppost',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
