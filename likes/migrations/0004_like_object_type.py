# Generated by Django 4.2.6 on 2023-11-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0003_alter_like_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='object_type',
            field=models.CharField(choices=[('post', 'post'), ('comment', 'comment')], default=('post', 'post'), max_length=255),
        ),
    ]