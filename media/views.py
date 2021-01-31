import os

from django.http import FileResponse

from dom2.settings import MEDIA_ROOT


def get_image(request, name):
    p = os.path.join(MEDIA_ROOT, 'images', name)
    return FileResponse(open(p, 'rb'), filename=name)
