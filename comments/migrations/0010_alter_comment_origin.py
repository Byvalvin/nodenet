# Generated by Django 4.2.6 on 2023-11-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0009_alter_comment_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='origin',
            field=models.TextField(blank=True, null=True),
        ),
    ]
