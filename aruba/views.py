from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Switches, Participants
from .forms import RegistrationForm
# Create your views here.

def index(request):
    switches = Switches.objects.all()
    return render(request, 'aruba/index.html', {
        'switches': switches
    })

def switches_details(request, switches_slug):
    try:
        selected_switches = Switches.objects.get(slug=switches_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participants = registration_form.save()
                selected_switches.participants.add(participants)
                print('going to redirect')
                return redirect('confirm-registration', switches_slug=switches_slug)
        return render(request, 'aruba/switches-details.html',{
                'switches_found': True,
                'switches': selected_switches,
                'form': registration_form
                })
    except Exception as exc:
        print(exc)
        return render(request,'aruba/switches-details.html',{
                'switches_found':False,
        })

def confirm_registration(request, switches_slug):
    switches = Switches.objects.get(slug=switches_slug)
    return render(request, 'aruba/registration-success.html', {
        'organizer_email': switches.organizer_email
    })