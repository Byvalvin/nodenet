# Generated by Django 4.2.6 on 2023-10-30 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0012_apppost_contentmarkdown_apppost_contentplain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apppost',
            name='contentType',
            field=models.CharField(blank=True, choices=[('plain', 'plain'), ('markdown', 'markdown'), ('hyperlink', 'hyperlink'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default='text/plain', max_length=255),
        ),
    ]
