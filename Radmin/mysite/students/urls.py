from django.urls import path, include
from django.views.generic import ListView, DetailView
from students.models import Student

urlpatterns = [ path('', ListView.as_view(queryset=Student.objects.all().order_by("-student_score")[:25],
                                                     template_name="students/students.html"))] 