# Generated by Django 4.2.6 on 2023-10-27 17:15

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0005_alter_apppost_categories_alter_apppost_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apppost',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='apppost',
            name='id',
            field=models.TextField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='apppost',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
