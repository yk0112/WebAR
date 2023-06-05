from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('markerbase', views.mb, name='mb'),
    path('camera', views.camera, name='camera'),
    path('add', views.add, name='add'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)