from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'GET':
        return HttpResponse("Metodo GET")
    return HttpResponse(request)