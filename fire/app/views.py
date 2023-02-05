from django.shortcuts import render
from .models import *

# Create your views here.
def sports(request, sport_id):
    sport = Sport.objects.get(pk=sport_id)
    discipline = Discipline.objects.filter(sport=sport)
    progress = Progress.objects.filter(sport=sport)
    trainer = Trainer.objects.filter(sport=sport)

    context = {'sport': sport,
               'discipline': discipline,
               'progress': progress,
               'trainer': trainer,
               }
    # return render(request, 'page32394306.html', context)
    return render(request, 'freestyle.html', context)