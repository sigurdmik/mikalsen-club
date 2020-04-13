from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader


def index(request):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render())
    
