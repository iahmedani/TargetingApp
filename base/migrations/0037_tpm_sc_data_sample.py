# Generated by Django 5.1 on 2024-10-06 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_remove_tpm_ee_data_ag_work_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tpm_sc_data',
            name='sample',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='tpm_records', to='base.sample1'),
        ),
    ]
