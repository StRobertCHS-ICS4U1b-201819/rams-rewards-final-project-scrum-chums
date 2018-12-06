from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.template import Context, loader
from .models import Activity, OneTimeActivity


#class ActivityListView(ListView):
#     model = Activity


def index(request):
#    lst = [activity.__str__() for activity in Activity.objects.all()]
    lst = Activity.objects.all()
    onetime = OneTimeActivity.objects.all()
#    return HttpResponse([activity.__str__() for activity in lst])
    template = loader.get_template("index.html")	
    context = Context({"activity_list": lst})
    return HttpResponse(template.render({'activity_list': lst, 'onetime_list': onetime}))