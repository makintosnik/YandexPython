import datetime as dt# Импортируйте необходимые модули

FORMAT = '%H:%M:%S' # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2:
        return False
    time_check, step_check = data
    if time_check == None or step_check == None:
        return False
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    len_storage_data = len(storage_data)
    if len_storage_data == 0:
        return True
    else:
        key = max(storage_data)
        storage_data_time = dt.datetime.strptime(key, FORMAT)
        storage_data_time = dt.datetime.time(storage_data_time)
        if time <= storage_data_time:
            return False
    


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    sum_step = 0
    for step in storage_data.values():
        sum_step += step
    sum_step += steps
    return sum_step
    
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.
    

def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    len_step = (steps * STEP_M) / 1000
    return len_step
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    hours = float(current_time.hour) + float(current_time.minute/60)
    minutes = hours * 60
    mean_speed = dist/hours
    spent_calories = (0.035*WEIGHT + (mean_speed**2 / HEIGHT) * 0.029*WEIGHT) * minutes
    return spent_calories
    # В уроке «Последовательности» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени; 
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.

def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        congratulation = f'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        congratulation = f'Неплохо! День был продуктивным.'
    elif dist >= 2:
        congratulation = f'Маловато, но завтра наверстаем!'
    else:
        congratulation = f'Лежать тоже полезно. Главное — участие, а не победа!'
    return congratulation
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.


# Место для функции show_message.
def show_message(pack_time, day_steps, dist, spent_calories, achievement):
    print(f'\nВремя: {pack_time}.\nКоличество шагов за сегодня: {day_steps}.\nДистанция составила {dist:.2f} км.\nВы сожгли {spent_calories:.2f} ккал.\n{achievement}\n')

def accept_package(data):
    """Обработать пакет данных."""

    if check_correct_data(data) == False:  # Если функция проверки пакета вернет False
        return 'Некорректный пакет'

    time, step = data# Распакуйте полученные данные.
    # Преобразуйте строку с временем в объект типа time.
    pack_time = dt.datetime.strptime(time, FORMAT)
    pack_time = dt.datetime.time(pack_time)
    
    if check_correct_time(pack_time) == False: 
    # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'

    day_steps = get_step_day(step) # Запишите результат подсчёта пройденных шагов.
    dist = get_distance(day_steps)  # Запишите результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, pack_time) # Запишите результат расчёта сожжённых калорий.
    achievement = get_achievement(dist) # Запишите выбранное мотивирующее сообщение.
    show_message(pack_time, day_steps, dist, spent_calories, achievement)# Вызовите функцию show_message().
    storage_data[time] = step# Добавьте новый элемент в словарь storage_data.
    return storage_data# Верните словарь storage_data.


# Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
