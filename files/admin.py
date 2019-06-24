from django.contrib import admin

from .models import (DataTrack, FileConfiguration, Files,
                     QuestionnaireConfiguration, StimulusConfiguration, Company, Solution, Job)


class FileConfigurationAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (
        'id', 'name', 'media_type', 'type_os'
    )
    ordering = ('id',)


class FilesAdmin(admin.ModelAdmin):
    """FilesAdmin describes to return files filter objects
    in admin panel.
    """
    list_display = ('id', 'name', 'file')
    ordering = ('id',)


class StimulusConfigurationAdmin(admin.ModelAdmin):
    """StimulusConfigurationAdmin describes to return stimulus
    configurations filter objects in admin panel.
    """
    list_display = (
        'id', 'name', 'type'
    )
    list_filter = ('type',)
    ordering = ('id',)
    list_editable = ('type',)


class QuestionnaireConfigurationAdmin(admin.ModelAdmin):
    """QuestionnaireConfigurationAdmin describes to return questionnaire
    configurations filter objects in admin panel.
    """
    list_display = (
        'uniq_key', 'name', 'stimulus'
    )
    ordering = ('uniq_key',)


class DataTrackAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'stimulus', 'questionnaire', 'time_started', 'time_ended'
    )
    ordering = ('id',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'short_name'
    )
    ordering = ('id',)


class SolutionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'short_name'
    )
    ordering = ('id',)


class JobAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'solution', 'research_company', 'respondent_limit'
    )
    ordering = ('id',)


admin.site.register(Files, FilesAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(FileConfiguration, FileConfigurationAdmin)
admin.site.register(StimulusConfiguration, StimulusConfigurationAdmin)
admin.site.register(QuestionnaireConfiguration, QuestionnaireConfigurationAdmin)
admin.site.register(DataTrack, DataTrackAdmin)
