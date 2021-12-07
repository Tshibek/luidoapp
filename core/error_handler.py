from django.shortcuts import render
from django.template import RequestContext


def handler404(request, exception):
    template_name="errors/404.html"
    return render(request, template_name, status_code = 404)

def handler500(request, exception):
    template_name="errors/500.html"
    return render(request, template_name, status_code = 500)