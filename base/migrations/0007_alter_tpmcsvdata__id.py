# Generated by Django 5.1 on 2024-08-17 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_csvdata_options_sample_cp_id_sample_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tpmcsvdata',
            name='_id',
            field=models.IntegerField(unique=True),
        ),
    ]
