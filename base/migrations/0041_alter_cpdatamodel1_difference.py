# Generated by Django 5.1 on 2024-10-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_alter_cpdatamodel1_cfac_calculation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpdatamodel1',
            name='difference',
            field=models.IntegerField(null=True),
        ),
    ]
