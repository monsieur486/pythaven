from django.http import HttpResponse
from django.views.decorators.http import require_GET
from rest_framework.response import Response


@require_GET
def hello(request):
    return HttpResponse("Hello, world. Coucou ma Darling c'est l'été :)")
