from django.shortcuts import render

# Create your views here.


def control(request):
    return render(request, 'control/base.html')


def publish(request):
    return render(request, 'control/publish.html')
