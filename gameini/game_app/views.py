"""App views."""
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from game_app.models import GameModel
from game_app.junk_drawer import ConfigSectionMap
from game_app.forms import GameForm, UploadForm
try:
    import ConfigParser as Config
except ImportError:
    import configparser as Config


def home_view(request):
    """Place holder view."""
    if request.method == 'POST':
        form = GameForm(request.POST)
        return redirect('files/{}'.format(form.data['games']))
    else:
        form = GameForm()
        upload_form = UploadForm()
        return render(request, 'home.html', context={'form': form, 'upload_form': upload_form})


def upload_view(request):
    """Upload file."""
    upload_form = UploadForm(request.POST, request.FILES)
    upload_form.save()
    query_title = upload_form.data['title']
    instance = GameModel.objects.get(title=query_title)
    return redirect('/generateform/{}'.format(instance.id))


def generate_form(request, **kwargs):
    """Generate form from uploaded file."""
    file_id = kwargs.get('file_id')
    file = GameModel.objects.filter(id=file_id).first()
    ConfigSectionMap(file.ini_file)


def download_file(request, **kwargs):
    """View file."""
    file_id = kwargs.get('file_id')
    file_object = GameModel.objects.filter(id=file_id).first()
    file_name = file_object.ini_file.name
    file = file_object.ini_file.read()
    response = HttpResponse(file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
    return response
