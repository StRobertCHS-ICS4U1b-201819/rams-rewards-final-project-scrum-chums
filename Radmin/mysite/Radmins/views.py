from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("my eyes hurt")

def index(request):
    return render(request, 'Radmins/home.html')
    
def contact(request):
    return render(request, 'Radmins/basic.html', {'content':["Email: robbie4lyfe@ycdsbk69.ca",
                                                             "Address: 8101 Leslie St, Thornhill, ON L3T 7P4",
                                                             "Phone: (905) 889-4982",
                                                             "Principal: Joseph Servidio"]})