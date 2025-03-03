from django.shortcuts import render

from works.models import Category, Project


# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def index(request):
    context = {
        'categories': Category.objects.all(),
        'projects': Project.objects.all(),

    }
    return render(request, 'landing-1.html',context)

def work(request):
    return render(request, 'landing-2.html')


