from rest_framework import routers
from .viewsets import IntervencionEstViewSet, SesionEstViewSet, SesionD1ViewSet, SesionD2ViewSet , SesionD3ViewSet , SesionD4ViewSet , SesionD5ViewSet , SesionD6ViewSet , SesionD7ViewSet , SesionD8ViewSet , SesionD9ViewSet

router = routers.SimpleRouter()
router.register(r'intervencion', IntervencionEstViewSet)
router.register(r'sesionD', SesionEstViewSet)
router.register(r'sesionD1', SesionD1ViewSet)
router.register(r'sesionD2', SesionD2ViewSet)
router.register(r'sesionD3', SesionD3ViewSet)
router.register(r'sesionD4', SesionD4ViewSet)
router.register(r'sesionD5', SesionD5ViewSet)
router.register(r'sesionD6', SesionD6ViewSet)
router.register(r'sesionD7', SesionD7ViewSet)
router.register(r'sesionD8', SesionD8ViewSet)
router.register(r'sesionD9', SesionD9ViewSet)


urlpatterns = router.urls