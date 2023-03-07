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

    list_progress = []     #Инициализирую список в котором будт схраниться словари
    for d in discipline:
        dict_progress = {}  #Инициализирую словарь для хранения информации по всей дисциплине + прогресс
        name = d.name
        description = d.description
        if 'name_discipline' and 'description_discipline' not in dict_progress:  #Проверка на наличие уже существующих ключей
            dict_progress['name_discipline'] = name
            dict_progress['description_discipline'] = description
        for pp in progress:
            list_info = []   #Инициализация списка для хранения словарей о прогрессе
            for p in pp:
                name_discipline = str(p.discipline_progress) #Приводим значение поля к типу строка
                if name_discipline == name:
                    dict_athlete = {}     #Инициализирую словарь информации по прогрессу
                    athlete = p.athlete
                    descr = p.description
                    dict_athlete['athlete_progress'] = athlete
                    dict_athlete['description_progress'] = descr
                    list_info.append(dict_athlete)   #Складываю полученный словарь в список
                    dict_progress['athlete_info'] = list_info #Складываю полученный список в словарь
        list_progress.append(dict_progress) #Складываю полученный словарь содержащий всю инфу по дисциплине  прогресс в список

    context = {'sport': sport,
               'discipline': discipline,
               'progress': progress,
               'trainer': trainer,
               'list_progress': list_progress,
               'p': p,
               }
    # return render(request, 'test.html', context)
    # return render(request, 'test3.html', context)
    return render(request, 'freestyle2.html', context)
    # return render(request, 'freestyle_good.html', context)


class SportListView(ListView):
    model = Sport
    context_object_name = 'sports'
    template_name = 'sports.html'
    queryset = Sport.objects.all()
