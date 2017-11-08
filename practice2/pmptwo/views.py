from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    helpPage = {'help_page': "this is help page view.py"}
    return render(request, 'help/help.html', context=helpPage)