from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("my eyes hurt")

def index(request):
    return render(request, 'Radmins/home.html')
    
def contact(request):
    return render(request, 'Radmins/basic.html', {'content':["If y'all wanna hit us up, shoot us an email real quick", "robbie4lyfe@ycdsbk69.ca"]})