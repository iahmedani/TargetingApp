# Generated by Django 5.1 on 2024-09-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_cpdatamodel_sb_nahia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpdatamodel1',
            name='SB_nahia',
            field=models.IntegerField(null=True),
        ),
    ]
