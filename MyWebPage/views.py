from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2><center>Hello World from Ukraine!</h2></center>")

