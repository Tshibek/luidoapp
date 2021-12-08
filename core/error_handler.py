from django.shortcuts import render
from django.template import RequestContext


def handler404(request, exception):
    context = {}
    response = render(request, 'errors/404.html', context=context)
    response.status_code = 404
    return response


def handler500(request, exception):
    context = {}
    response = render(request, 'errors/500.html', context=context)
    response.status_code = 500
    return response