from django.shortcuts import render
from .models import Gym, Route
from django.http import Http404

def index(request):
    return render(request, 'routeguide/index.html')

def indoor(request):
    all_gyms = Gym.objects.all()
    return render(request, 'routeguide/indoor.html', {'all_gyms': all_gyms})

def indoor_gym(request, gym_id):
    try:
        gym = Gym.objects.get(pk=gym_id)
    except Gym.DoesNotExist:
        raise Http404('Gym does not exist')

    return render(request, 'routeguide/gym.html', {'gym': gym})
