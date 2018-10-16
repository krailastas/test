from rest_framework.routers import SimpleRouter

from .views import QuestionnaireConfigurationViewSet, DataTrackViewSet, \
    AndroidFileViewSet, IOSFileViewSet


router = SimpleRouter(trailing_slash=False)
router.register(
    'stimulus/instance', QuestionnaireConfigurationViewSet,
    base_name='questionnaire_stimulus'
)
router.register(
    'datarecord/usage', DataTrackViewSet, base_name='datarecord_usage'
)
router.register(
    'file/ios', IOSFileViewSet, base_name='ios_files'
)
router.register(
    'file/android', AndroidFileViewSet, base_name='android_files'
)

urlpatterns = router.urls
