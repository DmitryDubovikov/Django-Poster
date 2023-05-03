from django.http import HttpResponse
from django.template import loader


def main(request):
    template = loader.get_template("main.html")
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def index(request):
    template = loader.get_template("index.html")
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
