from django.urls import include, path
from rest_framework import routers
from api_v1.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]