from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView
from django.http import JsonResponse

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

    list_progress = []
    for d in discipline:
        dict_progress = {}
        name = d.name
        description = d.description
        # if name not in list_progress:
        dict_progress['name_discipline'] = name
        dict_progress['description_discipline'] = description
        for pp in progress:
            for p in pp:
                name_discipline = str(p.discipline_progress)
                if name_discipline == name:
                    dict_athlete = {}
                    athlete = p.athlete
                    descr = p.description
                    dict_athlete['athlete_progress'] = athlete
                    dict_athlete['description_progress'] = descr
                    dict_progress['athlete_info'] = [dict_athlete]
                    list_progress.append(dict_progress)

    context = {'sport': sport,
               'discipline': discipline,
               'progress': progress,
               'trainer': trainer,
               'list_progress': list_progress,
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
