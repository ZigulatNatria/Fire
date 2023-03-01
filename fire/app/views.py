from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView

# Create your views here.
def sports(request, sport_id):
    sport = Sport.objects.get(pk=sport_id)
    discipline = Discipline.objects.filter(sport=sport_id)

# Циклом перебераем все сущности Progress по id Discipline
    progress = []
    for d in discipline:
        p = d.id
        prog = Progress.objects.filter(discipline_progress=p)
        progress.append(prog)
    trainer = Trainer.objects.filter(sport=sport)

    context = {'sport': sport,
               'discipline': discipline,
               'progress': progress,
               'trainer': trainer,
               'p': p,
               }
    # return render(request, 'test.html', context)
    return render(request, 'test3.html', context)
    # return render(request, 'freestyle.html', context)


class SportListView(ListView):
    model = Sport
    context_object_name = 'sports'
    template_name = 'sports.html'
    queryset = Sport.objects.all()
