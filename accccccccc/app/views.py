from django.shortcuts import render
#from .models import HomeFields
# Create your views here.


def Index(request):
    #data = HomeFields.objects.all()
    return render(request, 'index.html')


def Gallery(request):
    return render(request, 'gallery.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Review(request):
    return render(request, 'review.html')
