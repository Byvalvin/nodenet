# Generated by Django 4.2.6 on 2023-12-05 09:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0007_alter_like_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='id2',
            field=models.TextField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.TextField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='like',
            name='object_on',
            field=models.TextField(),
        ),
    ]
