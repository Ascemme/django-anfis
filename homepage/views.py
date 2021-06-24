from django.shortcuts import render
from icecream.models import icecream_db
from anfisa.models import friends_db
from anfisa.services import what_weather
# Импорт должен быть тут


def index(request):
    icecreams = ''
    friends = ''

    for friend in friends_db:
        # Узнайте город друга и сохраните его в city
        city = friends_db[friend]
        # Получите погоду из функции what_weather() и сохраните её в переменную weather
        weather = what_weather(city)
        # Здесь через f-строку объедините переменные в одну строчку:
        # имя :: город :: погода
        friends += f'{friend} :: {city} :: {weather} <br>'

    for i in range(len(icecream_db)):
        icecreams += (f'{icecream_db[i]["name"]} | '
                    f'<a href="icecream/{i}/">Узнать состав</a><br>')

    context = {
        'icecreams': icecreams,
        'friends': friends,
    }
    return render(request, 'homepage/index.html', context)
