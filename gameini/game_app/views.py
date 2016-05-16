"""App views."""
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from game_app.models import GameModel
from game_app.clean_files import config_section_map, change_settings, separate_sections
from game_app.forms import GameForm, UploadForm, SectionsForm


def home_view(request):
    """Home view."""
    if request.method == 'POST':
        form = GameForm(request.POST)
        return redirect('/sections/{}'.format(form.data['games']))
    else:
        form = GameForm()
        upload_form = UploadForm()
        return render(request, 'home.html', context={'form': form, 'upload_form': upload_form})


def upload_view(request):
    """Upload file."""
    upload_form = UploadForm(request.POST, request.FILES)
    instance = upload_form.save()
    return redirect('/sections/{}'.format(instance.id))


def grab_sections(request, **kwargs):
    """Create Drop Down with file's sections."""
    file_id = kwargs.get('file_id')
    game_file = GameModel.objects.filter(id=file_id).first().ini_file.file
    if request.method == 'POST':
        # SectionsForm(request.POST)
        section = request.POST['game_sections']
        return redirect('/generateform/{}/{}'.format(file_id, section))
    sections = separate_sections(game_file)
    sections_form = SectionsForm(sections)
    return render(request, 'home.html', context={'sections_form': sections_form})


def generate_form(request, **kwargs):
    """Generate form based on game file settings."""
    import pdb; pdb.set_trace()
    file_id = kwargs.get('file_id')
    file = GameModel.objects.filter(id=file_id).first()
    parsed_file, section = config_section_map(file.ini_file.file)
    if request.method == 'GET':
        return render(request, 'home.html', context={'parsed_file': parsed_file})
    form_data = request.POST
    copy = file.ini_file.file
    temp = change_settings(section, form_data, copy)
    temp.seek(0)
    response = HttpResponse(temp, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={}.ini'.format(file.title)
    temp.close()
    return response

