import random

def get_char_date(date):
    day_set = ('первое', 'второе', 'третье', 'четвёртое',
               'пятое', 'шестое', 'седьмое', 'восьмое',
               'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
               'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
               'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
               'двадцать первое', 'двадцать второе', 'двадцать третье',
               'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
               'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
               'тридцатое', 'тридцать первое')

    month_set = ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря')

    return (f"{day_set[int(date[0]) - 1]} {month_set[int(date[1]) - 1]} {date[2]} года ")

def check_date(question, name, val):
    answer = input('{}{}: '.format(question, name))
    if answer == val:
        print('Верно!')
        return True

    i = 3
    while i > 0:
        answer = input(f'Не верно! {question} {name} количество оставщихся попыток = {i} : ')
        if answer == val:
            print('Верно!')
            return True
        else:
            i -= 1
    return False
def get_fameus_person():
    fameus_person = {
        'Исаак Ньютон': '25.12.1642',
        'Конфуций': '28.10.-551',
        'Николай Коперник': '19.02.1473',
        'Наполеон I': '05.05.1769',
        'Людвиг ван Бетховен': '26.03.177 ',
        'Александр Белл': '03.03.1847',
        'Макс Планк': '04.10.1858',
        'Вильгельм Рентген': '27.03.1845',
        'Иоганн Кеплер': '15.11.1571',
        'Энрико Ферми': '28.11.1901'
    }
    waste_message = 'Вы проиграли'
    name, date = random.choice(list(fameus_person.items()))
    date = date.split('.')
    if not  check_date('Введите день рождения для ', name, date[0]):
       print(waste_message)
       return
    elif not check_date('Введите месяц рождения для ', name, date[1]):
        print(waste_message)
        return
    elif not check_date('Введите год рождения для ', name, date[2]):
        print(waste_message)
        return
    else:
        print('Вы выиграли!')
        print(get_char_date(date))

#if __name__ == '__main__':
#    get_fameus_person()