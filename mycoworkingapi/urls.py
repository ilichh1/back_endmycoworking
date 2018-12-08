from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.views.static import serve
from rest_framework import routers
from points.views import *
from rest_framework.authtoken import views
router = routers.DefaultRouter()

router.register('Location', LocationViewSet)
router.register('Team', TeamViewSet)
router.register('User', UserViewSet)
router.register('User_team',User_teamViewSet)
router.register('Local', LocalViewSet)
router.register('Space', SpaceViewSet)
router.register('Coworking', CoworkingViewSet)
router.register('Status', StatusViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)), 
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
 ]
# cambio