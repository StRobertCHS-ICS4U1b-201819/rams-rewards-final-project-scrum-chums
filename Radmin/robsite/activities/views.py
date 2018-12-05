from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Activity 


#class ActivityListView(ListView):
#     model = Activity


def index(request):
    lst = Activity.objects.all()
    return HttpResponse([activity.__str__() for activity in lst])
