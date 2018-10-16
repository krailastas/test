from rest_framework.routers import SimpleRouter

from .views import LoginViewSet


router = SimpleRouter(trailing_slash=False)
router.register(
    'login', LoginViewSet,
    base_name='login'
)

urlpatterns = router.urls
