from django.shortcuts import render, HttpResponse, redirect
from . import models
import json
from json import JSONEncoder

def index(request):
    class Date:
        def __init__(self, ty, ly, difference):
            self.ty = ty
            self.ly = ly
            self.difference = difference
    def dateDecoder(obj):
        return Date(obj['ty'], obj['ly'], obj['difference'])
    dates = json.loads('June.json',
           object_hook=dateDecoder)
    context = {
        'ty': dates.TY,
        'ly': dates.LY,
        'difference': dates.difference,
    }
    return render(request, 'index.html', context)
