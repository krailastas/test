from rest_framework import mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import QuestionnaireConfigurationSerializer, \
    DataTrackSerializer, FileSerializer
from .models import QuestionnaireConfiguration, TypeOS, Files


class QuestionnaireConfigurationViewSet(mixins.RetrieveModelMixin,
                                        GenericViewSet):
    """
            **QuestionnaireConfigurationViewSet**

            Return stimulus.

            **list fields:**
            * 'id'
            * 'name'
            * 'type'
            * 'files' - list

            **TYPE_OS**
            * 'ANDROID = 1'
            * 'IOS = 2'

            **filters:**
            * `?operating_system=<integer>`
    """
    permission_classes = (AllowAny,)
    serializer_class = QuestionnaireConfigurationSerializer
    operating_system = None

    def get_queryset(self):
        os = self.request.GET.get('operating_system')
        self.operating_system = int(os) \
            if os and os.isdigit() and int(os) in (TypeOS.ANDROID, TypeOS.IOS) \
            else None
        return QuestionnaireConfiguration.objects.select_related(
            'stimulus'
        ).prefetch_related('stimulus__android_files', 'stimulus__ios_files')


class DataTrackViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = DataTrackSerializer
    permission_classes = (AllowAny,)


class FileMixinViewSet(mixins.RetrieveModelMixin,
                       GenericViewSet):
    serializer_class = FileSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            instance = self.get_queryset().get(**filter_kwargs)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Files.DoesNotExist:
            return Response(
                {'errors': 'File doesn\'t exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )


class AndroidFileViewSet(FileMixinViewSet):

    def get_queryset(self):
        return Files.objects.filter(file_configuration__type_os=TypeOS.ANDROID)


class IOSFileViewSet(FileMixinViewSet):

    def get_queryset(self):
        return Files.objects.filter(file_configuration__type_os=TypeOS.IOS)
