from django.http import HttpResponse

# Create your views here.
def hello(request, s):
    return HttpResponse(f'Hello, {s} world!')

