from django.http import HttpResponse

# To call this view file, we need to map it to a URL - and for this we need a URLconf which is created in a file called urls.py
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
