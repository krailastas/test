# Generated by Django 2.0.4 on 2019-06-24 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0009_auto_20181003_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255)),
                ('short_name', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='DataRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondent_limit', models.PositiveIntegerField(default=1)),
                ('research_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.Company')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255)),
                ('short_name', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Solution',
                'verbose_name_plural': 'Solutions',
            },
        ),
        migrations.AlterModelOptions(
            name='fileconfiguration',
            options={'verbose_name': 'File configurations (FC)', 'verbose_name_plural': 'File configurations (FC)'},
        ),
        migrations.AlterModelOptions(
            name='questionnaireconfiguration',
            options={'verbose_name': 'Stimulus Instance (SI)', 'verbose_name_plural': 'Stimulus Instance (SI)'},
        ),
        migrations.AlterModelOptions(
            name='stimulusconfiguration',
            options={'verbose_name': 'Stimulus configurations (SC)', 'verbose_name_plural': 'Stimulus configurations (SC)'},
        ),
        migrations.AddField(
            model_name='job',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.Solution'),
        ),
        migrations.AddField(
            model_name='datarecord',
            name='si',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_datarecords', to='files.QuestionnaireConfiguration'),
        ),
    ]
