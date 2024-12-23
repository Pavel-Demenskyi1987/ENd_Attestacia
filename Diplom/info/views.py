from django.shortcuts import render


def rules(request):
    temp = 'info/rules.html'
    return render(request, temp)


def about(request):
    temp = 'info/about.html'
    return render(request, temp)
# Create your views here.
