from django.urls import path

from media.views import get_image
app_name = 'media'

urlpatterns = [
    path('images/<str:name>', get_image, name='get-image')
]
