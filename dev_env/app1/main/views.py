from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page':'Home - это  современное предприятие, специализирующееся на производстве и продаже мебели по индивидуальным размерам заказчика. Компания успешно работает на мебельном рынке с 2005 года. В собственности компании более 12 000 м.кв. производственных площадей, на которых расположено современное оборудование известных мировых брендов. В компании трудится более 30 опытных дизайнеров и имеется собственная бригада профессиональных монтажников, а также большой конструкторский отдел и собственный парк грузовых автомобилей.',

    }
    return render(request, 'main/about.html', context)

def contact(request):
    context = {
        'title': 'Home - Контактная информация',
        'content': 'Контактная информация',
        'text_on_page':'Часы работы: Будни: с 09:00 до 18:00 Выходные: Сб, Вс. \n Связаться с нами: +7 (343) 537-93-01, +7 (932) 129-64-45, email: home-furniture@gmail.com. \n Адрес: Екатеринбург, Балакинская, 64/3',
    }
    return render(request, 'main/about.html', context)