from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Homepage! <br/> <a href='/rango/about'>Go To About Page</a>")

def about(request):
    return HttpResponse("Just bored. Keeping Busy. <br/> <a href='/rango/'>Back To Homepage</a>")