from .views import rules, about
from django.urls import path

app_name = 'info'
urlpatterns = [
    path('rules/', rules, name='rules'),
    path('about/', about, name='about'),
]
