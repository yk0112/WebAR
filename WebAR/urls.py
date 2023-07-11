from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('markerbase', views.mb, name='mb'),
    path('camera_mb', views.camera_mb, name='camera_mb'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('locationbase', views.lb, name='lb'),
    path('face', views.face, name='face'),
    path('camera_lb', views.camera_lb, name='camera_lb'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)