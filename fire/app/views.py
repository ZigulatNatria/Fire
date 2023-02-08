from django.shortcuts import render
from .models import *

# Create your views here.
def sports(request, sport_id):
    sport = Sport.objects.get(pk=sport_id)
    discipline = Discipline.objects.get(sport=sport_id)
    # discipline_id = discipline.objects.get()
    progress = Progress.objects.filter(discipline_progress=discipline.pk)
    trainer = Trainer.objects.filter(sport=sport)

    context = {'sport': sport,
               'discipline': discipline,
               'progress': progress,
               'trainer': trainer,
               }
    # return render(request, 'test.html', context)
    return render(request, 'freestyle.html', context)