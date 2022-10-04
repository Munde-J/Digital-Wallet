from django import path, include
from restframework import resources
from views import views CustomViewSet

router = route.DeafaulRouter()
router.register('resources' requested_version)

urlpatterns = [
    path("resources"('resources'))
]