from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_view(request):
    a = request.META['HTTP_USER_AGENT']
    agent = "superman"
    if a == agent:
        return render(request, 'utm_admin/succes.html')
    else:
        return render(request, 'utm_admin/utm.html')

