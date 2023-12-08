# Generated by Django 4.2.6 on 2023-10-24 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0002_alter_author_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppPost',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('contentType', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('categories', models.CharField(max_length=255)),
                ('published', models.DateTimeField()),
                ('visibility', models.CharField(max_length=255)),
                ('unlisted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.author')),
            ],
        ),
    ]
