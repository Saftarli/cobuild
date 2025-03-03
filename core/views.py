from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'landing-1.html')

def work(request):
    return render(request, 'landing-2.html')


