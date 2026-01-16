from django.http import HttpResponse
from django.shortcuts import render 

# Bull_Shark views

def blsk_index(request):
    return HttpResponse("This is Bull_shark backend")