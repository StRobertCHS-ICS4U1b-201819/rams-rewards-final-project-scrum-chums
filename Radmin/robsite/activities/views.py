from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.template import Context, loader
from .models import Activity, OneTimeActivity
from datetime import date

#class ActivityListView(ListView):
#     model = Activity


def index(request):
#    lst = [activity.__str__() for activity in Activity.objects.all()]
    all_list = Activity.objects.all()
    onetime = OneTimeActivity.objects.all()
    upcoming = OneTimeActivity.objects.filter(activity_date__gte=date.today()).order_by("activity_date")
    past = OneTimeActivity.objects.filter(activity_date__lt=date.today()).order_by("-activity_date")
#    return HttpResponse([activity.__str__() for activity in lst])
    template = loader.get_template("index.html")
    context = Context({"activity_list": all_list})
    return HttpResponse(template.render({'activity_list': all_list, 'onetime_list': onetime, 'upcoming_list': upcoming, 'past_list': past}))