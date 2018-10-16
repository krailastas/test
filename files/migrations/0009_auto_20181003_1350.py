# Generated by Django 2.0.4 on 2018-10-03 13:50

from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0008_auto_20181003_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionnaireconfiguration',
            options={'verbose_name': 'Stimulus Instance (SA)', 'verbose_name_plural': 'Stimulus Instance (SA)'},
        ),
        migrations.RemoveField(
            model_name='questionnaireconfiguration',
            name='id',
        ),
        migrations.AddField(
            model_name='questionnaireconfiguration',
            name='uniq_key',
            field=models.CharField(default=files.models._createId, max_length=256, primary_key=True, serialize=False),
        ),
    ]
