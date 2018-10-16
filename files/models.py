from django.db import models

from binascii import hexlify
import os

from .helps import get_file_path


class FilesType:
    VIDEO = 1
    ASSETBUNDLE = 2

    TYPE_CHOICES = (
        (VIDEO, 'Video'),
        (ASSETBUNDLE, 'ASSETBUNDLE')
    )


class TypeOS:
    ANDROID = 1
    IOS = 2

    TYPE_CHOICES = (
        (ANDROID, 'Android'),
        (IOS, 'IOS')
    )


class TypeStimulus:
    AR = 1
    VR = 2

    TYPE_CHOICES = (
        (AR, 'AR'),
        (VR, 'VR')
    )


class AbstractName(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Files(AbstractName):
    file = models.FileField(
        upload_to=get_file_path, blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    file_configuration = models.ForeignKey(
        'files.FileConfiguration', null=True,
        related_name='file_configurations', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'


class FileConfiguration(AbstractName):
    media_type = models.IntegerField(
        choices=FilesType.TYPE_CHOICES, default=FilesType.VIDEO
    )
    type_os = models.IntegerField(
        choices=TypeOS.TYPE_CHOICES, default=TypeOS.ANDROID
    )


class StimulusConfiguration(AbstractName):
    type = models.IntegerField(
        choices=TypeStimulus.TYPE_CHOICES, default=TypeStimulus.AR
    )
    android_files = models.ManyToManyField(
        'files.Files', related_name='files_android_list',
        limit_choices_to={'file_configuration__type_os': TypeOS.ANDROID},
        blank=True, null=True
    )
    ios_files = models.ManyToManyField(
        'files.Files', related_name='files_ios_list',
        limit_choices_to={'file_configuration__type_os': TypeOS.IOS},
        blank=True, null=True
    )


def _createId():
    return hexlify(os.urandom(4)).decode('utf-8')


class QuestionnaireConfiguration(AbstractName):
    stimulus = models.ForeignKey(
        'files.StimulusConfiguration', related_name='stimulus_questionnaires',
        on_delete=models.CASCADE
    )
    uniq_key = models.CharField(max_length=256, primary_key=True, default=_createId)

    class Meta:
        verbose_name = 'Stimulus Instance (SA)'
        verbose_name_plural = 'Stimulus Instance (SA)'


class DataTrack(models.Model):
    stimulus = models.ForeignKey(
        'files.StimulusConfiguration', related_name='stimulus_datatracks',
        blank=True, null=True, on_delete=models.CASCADE
    )
    questionnaire = models.ForeignKey(
        'files.QuestionnaireConfiguration',
        related_name='questionnaire_datatracks',
        blank=True, null=True, on_delete=models.CASCADE
    )
    time_started = models.DateTimeField()
    time_ended = models.DateTimeField()


class DataRecord(models.Model):
    si = models.ForeignKey(
        'files.QuestionnaireConfiguration',
        related_name='questionnaire_datarecords',
        blank=True, null=True, on_delete=models.CASCADE
    )


# class Locations(models.Model):
#     record = models.ForeignKey('files.DataRecord', related_name='datarecord_locations', on_delete=models.CASCADE)
#     postcode = models.CharField(max_length=128, blank=True)
#     city = models.CharField(max_length=128, blank=True)
#     country = models.CharField(max_length=128, blank=True)
#     continent = models.CharField(max_length=128, blank=True)
#     xs = models.FloatF

