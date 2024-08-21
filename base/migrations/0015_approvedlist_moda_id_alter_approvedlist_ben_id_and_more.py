# Generated by Django 5.1 on 2024-08-18 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_tpmcsvdata_sample_alter_sample_sample_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvedlist',
            name='moda_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='approvedlist',
            name='ben_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.csvdata'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='modaprojects',
            name='project_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='modauser',
            name='moda_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='targetingforms',
            name='form_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='cfaclist',
            unique_together={('name', 'province', 'district')},
        ),
        migrations.AlterUniqueTogether(
            name='cp_list',
            unique_together={('name', 'province')},
        ),
        migrations.AlterUniqueTogether(
            name='tpm_list',
            unique_together={('name', 'province')},
        ),
        migrations.AlterUniqueTogether(
            name='villagelist',
            unique_together={('name', 'district_code')},
        ),
    ]
