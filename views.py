from django.http import Httpresponse


def index(request):
    return HttpResponse("INDEX")
