# импорт библиотеки datetime
import datetime
# получение текущей даты
def get_current_date():
    return datetime.datetime.now()
# расчёт разницы между датами
def calculate_date_difference(date1, date2):
    return (date2 - date1).days
# Функция для обработки пользовательского ввода
def get_user_input():
    while True:
        try:
            user_input = input("Введите дату дедлайна (в формате день.месяц.год): ")
            deadline_date = datetime.datetime.strptime(user_input, "%d.%m.%Y")
            return deadline_date
        except ValueError:
            print("Пожалуйста, введите дату в формате день-месяц-год, например: 10.12.2024.")
# проверка сроков дедлайна
def check_deadline(deadline_date):
    current_date = get_current_date()
    date_difference = calculate_date_difference(current_date, deadline_date)
    if date_difference < 0:
        print("Внимание! Дедлайн истёк", abs(date_difference), "дней назад.")
    elif date_difference == 0:
        print("Дедлайн сегодня!")
    else:
        print("До дедлайна осталось", date_difference, "дней.")
# запуск программы
def run_program():
    print("Текущая дата:", get_current_date().strftime("%d.%m.%Y"))
    deadline_date = get_user_input()
    check_deadline(deadline_date)
run_program()