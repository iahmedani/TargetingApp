# Generated by Django 5.1 on 2024-09-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rename__submission_time_cpdatamodel_submissiondate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpdatamodel',
            name='id_r',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
