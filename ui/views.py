from django.shortcuts import render

from ui.models import Pictogram


def index(request):
    return render(request, 'index.html', {'pictograms': Pictogram.objects.all()})

#TODO add an upload view and corresponding template

#TODO allow user to choose which icon and voice sets to load
