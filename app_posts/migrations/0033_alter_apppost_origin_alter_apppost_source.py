# Generated by Django 4.2.6 on 2023-11-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0032_alter_apppost_origin_alter_apppost_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apppost',
            name='origin',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apppost',
            name='source',
            field=models.TextField(blank=True, null=True),
        ),
    ]
