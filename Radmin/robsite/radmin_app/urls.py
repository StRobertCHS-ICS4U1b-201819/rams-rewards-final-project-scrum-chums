from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='activities'),
	path('', views.student_display, name='students')
]