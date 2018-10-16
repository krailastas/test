# Generated by Django 2.0.4 on 2018-06-08 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20180608_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stimulusconfiguration',
            name='files',
        ),
        migrations.RemoveField(
            model_name='stimulusconfiguration',
            name='type_os',
        ),
        migrations.AddField(
            model_name='stimulusconfiguration',
            name='android_files',
            field=models.ManyToManyField(limit_choices_to={'file_configuration__type_os': 1}, related_name='files_android_list', to='files.Files'),
        ),
        migrations.AddField(
            model_name='stimulusconfiguration',
            name='ios_files',
            field=models.ManyToManyField(limit_choices_to={'file_configuration__type_os': 2}, related_name='files_ios_list', to='files.Files'),
        ),
    ]
