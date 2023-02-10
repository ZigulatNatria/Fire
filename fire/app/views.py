from django.shortcuts import render
from .models import *

# Create your views here.
def sports(request, sport_id):
    contacts = Contacts.objects.all()
    sport = Sport.objects.get(pk=sport_id)
    trainer = Trainer.objects.filter(sport=sport)
    discipline = Discipline.objects.filter(sport=sport_id)
    progress = Progress.objects.filter(sport=sport_id)

    context = {'sport': sport,
               'discipline': discipline,
               'trainer': trainer,
               'contacts': contacts,
               'progress': progress
               }
    return render(request, 'test.html', context)
    # return render(request, 'freestyle.html', context)