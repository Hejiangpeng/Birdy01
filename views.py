from django.http import Httpresponse
from django.shotcuts import redirect


def index(request):
    return HttpResponse("INDEX")

def login(request):
    return redirect("/index")
