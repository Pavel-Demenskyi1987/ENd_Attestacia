from django.shortcuts import render
from .models import Recipe
from .form import FindName, EntryName

def index(request):
    temp = 'recipe/index.html'
    data = Recipe.objects.all()
    # print(data)
    context = {'names': data}
    return render(request, temp, context)


def detail(request, pk):
    temp = 'recipe/detail.html'
    object = Recipe.objects.get(id=pk)
    context = {'data': object}
    return render(request, temp, context)


def find_name(request):
    form = FindName(request.GET or None)
    if form.is_valid():
        name = request.GET['name']
        temp = 'recipe/detail.html'
        data = Recipe.objects.get(name=name)
        context = {'data': data}
        return render(request, temp, context)
    else:
        temp = 'recipe/find_name.html'
        form = FindName()
        context = {'form': form}
        return render(request, temp, context)


def entry_name(request):
    temp = 'recipe/entry_name.html'
    instance = None
    form = EntryName(request.POST or None, files=request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, temp, context)
# Create your views here.


