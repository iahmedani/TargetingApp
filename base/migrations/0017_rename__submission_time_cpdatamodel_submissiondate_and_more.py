# Generated by Django 5.1 on 2024-09-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_rename_ben_id_approvedlist_cp_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpdatamodel',
            old_name='_submission_time',
            new_name='SubmissionDate',
        ),
        migrations.RenameField(
            model_name='cpdatamodel',
            old_name='HH_head_1',
            new_name='isValidated',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='HH_head_2',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='HH_head_3',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='HH_head_4',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='HH_head_5',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='HH_head_6',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='_duration',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='_id',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='_submitted_by',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='_uuid',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='_xform_id',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='female_status_1',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='female_status_2',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='female_status_3',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='female_status_4',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='female_status_5',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='female_status_6',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='female_status_7',
        ),
        migrations.RemoveField(
            model_name='cpdatamodel',
            name='female_status_8',
        ),
        migrations.AddField(
            model_name='cpdatamodel',
            name='HH_head',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='cpdatamodel',
            name='display',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cpdatamodel',
            name='female_status',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='cpdatamodel',
            name='formhub_uuid',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='cpdatamodel',
            name='infonote',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='cpdatamodel',
            name='key',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cpdatamodel',
            name='note',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cpdatamodel',
            name='tit',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='cpdatamodel',
            name='vul_note',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cpdatamodel',
            name='ag_work',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='cpdatamodel',
            name='id_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cpdatamodel',
            name='iom_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cpdatamodel',
            name='is_principal',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='cpdatamodel',
            name='mob',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cpdatamodel',
            name='observation',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='cpdatamodel',
            name='vul',
            field=models.CharField(max_length=10),
        ),
    ]
