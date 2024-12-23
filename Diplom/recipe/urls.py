from .views import index, detail, find_name, entry_name
from django.urls import path

app_name = 'recipe'
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('find_name/', find_name, name='find_name'),
    path('entry_name/', entry_name, name='entry_name'),
]
