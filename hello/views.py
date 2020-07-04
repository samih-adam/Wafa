from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

# Create your views here.
