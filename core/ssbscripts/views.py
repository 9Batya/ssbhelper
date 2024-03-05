from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import share_smart_house, NameForm
from django.core.mail import send_mail

def index(request):
    return render(request, "index.html")

def smarthouse(request):
    smartform = share_smart_house()


    return render(request, "ssbscripts/smarthouse.html", {'form': smartform})


def test(request):
    # if this is a POST request we need to process the form data
    form = NameForm()
    return render(request, "ssbscripts/name.html", {'form': form})