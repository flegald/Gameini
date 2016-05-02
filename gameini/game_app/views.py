"""App views."""
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import GameModel


def placeholder(request):
    """Place holder view."""
    return render(request, 'placeholder.html')


def view_file(request, **kwargs):
    """View file."""
    # import pdb; pdb.set_trace()
    file_id = kwargs.get('file_id')
    file_object = GameModel.objects.filter(id=file_id).first()
    file_name = file_object.ini_file.name
    file = file_object.ini_file.read()
    response = HttpResponse(file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
    return response


def download_file(request, file_name):
    """Download ini file."""
    file = GameModel.objects.get(title=file_name).ini_file.name
    file = file.split('/')[-1]
    response = HttpResponse
