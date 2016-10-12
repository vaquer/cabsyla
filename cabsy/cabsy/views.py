import os
import qrcode
from qrcode.image.pure import PymagingImage
from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html', {})
