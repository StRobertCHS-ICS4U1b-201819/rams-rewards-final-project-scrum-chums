from django.urls import path, include
from django.views.generic import ListView, DetailView
from activities.models import Activitie

urlpatterns = [ path('', ListView.as_view(queryset=Activitie.objects.all().order_by("-date")[:25],
                                                     template_name="activities/activities.html")),
                path('<int:pk>/', DetailView.as_view(model = Activitie,
                                                        template_name = "activities/post.html")),] 
                