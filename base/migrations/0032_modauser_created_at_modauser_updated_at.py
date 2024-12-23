# Generated by Django 5.1 on 2024-10-06 04:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_alter_targetingforms_moda_media_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='modauser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modauser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
