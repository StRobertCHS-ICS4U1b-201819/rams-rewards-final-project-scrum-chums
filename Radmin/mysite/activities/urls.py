from django.urls import path, include
from django.views.generic import ListView, DetailView
from activities.models import Activitie

urlpatterns = [ path('', ListView.as_view(queryset=Activitie.objects.all().order_by("-date")[:25],
                                                     template_name="activities/activities.html")),
                path('<int:pk>/', DetailView.as_view(model = Activitie,
                                                        template_name = "activities/post.html")),] 
                
# begins after /activities
# pk is primary digit
#\d+ means it's a digit. One or more digits in the number (pk??)
# It's a new Django so we ain't using urls(), we using path() so instead of Regular Expression (?P<pk>\d+),
# use <int:pk> now. b l e s s e d
# https://www.reddit.com/r/djangolearning/comments/8iompj/regular_expression_ppkd/