from django.shortcuts import get_object_or_404, render

from .models import Riddle, Option


def index(request):
    return render(request, "index.html",
                  {"latest_riddles": Riddle.objects.order_by('-pub_date')})


def detail(request, riddle_id):
    return render(request, "answer.html",
                  {"riddle": get_object_or_404(Riddle, pk=riddle_id)})


def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk=riddle_id)
    try:
        option = riddle.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render(request, 'answer.html',
                      {'riddle': riddle,
                       'error_message': 'нет такого варианта ответа'})
    else:
        if option.correct:
            return render(
                request, "index.html",
                {"latest_riddles": Riddle.objects.order_by('-pub_date'),
                 "message": "Правильно! Выбери ещё вопрос"})
        else:
            return render(request, 'answer.html',
                          {'riddle': riddle,
                           'error_message': 'Неверный ответ!'})
