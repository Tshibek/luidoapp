from django.shortcuts import render
from django.template import RequestContext


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'errors/error_404.html', data)


def handler500(request, exception):
    context = {}
    response = render(request, 'errors/500.html', context=context)
    response.status_code = 500
    return response