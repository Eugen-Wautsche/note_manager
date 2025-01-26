# импорт библиотеки datetime
import datetime


# получение текущей даты
def get_current_date():
    return datetime.datetime.now()


# расчёт разницы между датами
def calculate_date_difference(date1, date2):
    return (date2 - date1).days


# ввод
def get_user_input():
    while True:
        try:
            issue_date = input("Введите дату дедлайна (в формате день.месяц.год): ")
            issue_date = datetime.datetime.strptime(issue_date, "%d.%m.%Y")
            if issue_date < get_current_date():
                print("Пожалуйста, введите дату в будущем.")
            else:
                return issue_date
        except ValueError:
            print("Пожалуйста, введите дату в формате день.месяц.год, например: 10.12.2024.")


# проверка истечения дедлайна
def check_deadline(issue_date):
    current_date = get_current_date()
    date_difference = calculate_date_difference(current_date, issue_date)
    if date_difference < 0:
        print("Внимание! Дедлайн истёк", abs(date_difference), "дней назад.")
    elif date_difference == 0:
        print("Дедлайн сегодня!")
    else:
        print("До дедлайна осталось", date_difference, "дней.")


# запуск программы
def run_program():
    print("Текущая дата:", get_current_date().strftime("%d.%m.%Y"))
    issue_date = get_user_input()
    check_deadline(issue_date)


run_program()
