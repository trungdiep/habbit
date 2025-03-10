from django.http import HttpResponse


def index(request):
    print(request.test)
    return HttpResponse('Hello world')