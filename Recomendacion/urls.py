from rest_framework import routers

from .viewsets import  RecomendacionEstViewSet, RecomendacionD1ViewSet, RecomendacionD2ViewSet, RecomendacionD3ViewSet, RecomendacionD4ViewSet, RecomendacionD5ViewSet, RecomendacionD6ViewSet, RecomendacionD7ViewSet, RecomendacionD8ViewSet, RecomendacionD9ViewSet

router = routers.SimpleRouter()
router.register('recomendacionEst', RecomendacionEstViewSet)
router.register('recomendacionD1', RecomendacionD1ViewSet)
router.register('recomendacionD2', RecomendacionD2ViewSet)
router.register('recomendacionD3', RecomendacionD3ViewSet)
router.register('recomendacionD4', RecomendacionD4ViewSet)
router.register('recomendacionD5', RecomendacionD5ViewSet)
router.register('recomendacionD6', RecomendacionD6ViewSet)
router.register('recomendacionD7', RecomendacionD7ViewSet)
router.register('recomendacionD8', RecomendacionD8ViewSet)
router.register('recomendacionD9', RecomendacionD9ViewSet)


urlpatterns = router.urls

