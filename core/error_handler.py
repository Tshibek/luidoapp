from django.shortcuts import render
from django.template import RequestContext


def handler404(request, exception):
    template_name="errors/404.html"
    response = render(request, template_name)
    response.status_code = 404
    return response