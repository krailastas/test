from rest_framework import serializers

from .models import QuestionnaireConfiguration, DataTrack, Files, FilesType, \
    TypeOS


class QuestionnaireConfigurationSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.stimulus_id

    def get_name(self, obj):
        return obj.stimulus.name

    def get_type(self, obj):
        return obj.stimulus.type

    def get_files(self, obj):
        view = self.context['view']
        operating_system = view.operating_system
        if operating_system:
            if operating_system == TypeOS.ANDROID:
                qs = obj.stimulus.android_files.all()
            else:
                qs = obj.stimulus.ios_files.all()
            return [
                {
                    'id': o.id,
                    'type': 'video'
                    if o.file_configuration.media_type == FilesType.VIDEO
                    else 'assetbundle'
                } for o in qs
            ]
        else:
            qs = obj.stimulus.android_files.all()
            d = []
            for o in qs:
                d.append(
                    {
                        'id': o.id,
                        'type': 'video'
                        if o.file_configuration.media_type == FilesType.VIDEO
                        else 'assetbundle'
                    }
                )
            qs = obj.stimulus.ios_files.all()
            for o in qs:
                d.append(
                    {
                        'id': o.id,
                        'type': 'video'
                        if o.file_configuration.media_type == FilesType.VIDEO
                        else 'assetbundle'
                    }
                )
            return d

    class Meta:
        model = QuestionnaireConfiguration
        fields = ('id', 'name', 'type', 'files')


class DataTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTrack
        fields = (
            'id', 'questionnaire', 'stimulus',
            'time_started', 'time_ended'
        )


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ('id', 'file', 'created')
