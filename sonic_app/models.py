from django.db import models
import json
import datetime
import time

class Date:
    def __init__(self, ty, ly, difference):
        self.ty = ty
        self.ly = ly
        self.difference = difference

def dateDecoder(obj):
        return Date(obj['ty'], obj['ly'], obj['difference'])

