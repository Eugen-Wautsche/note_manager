info = 'Турбонапоминалка'
print(info)
username = input('Введите имя: ')
title = input('Заголовок заметки: ')
content = input('Описание заметки: ')
status = input('Статус заметки: ')
#Включаем модуль даты для проверки корректности
import datetime
#переходим в 1 цикл проверки формата даты
while True:
    created_date = input('Дата заметки в формате (день.месяц.год),например 10.11.2024: ')
    try:
        datetime.datetime.strptime(created_date,'%d.%m.%Y')
        print('Введена корректная дата')
        break
    except ValueError:
        print("Дата введена не корректно")
#переходим в 2 цикл проверки формата даты
while True:
    issue_date = input('Дедлайн в формате (день.месяц.год),например 18.01.2025: ')
    try:
        datetime.datetime.strptime(issue_date, '%d.%m.%Y')
        print('Введена корректная дата')
        break
    except ValueError:
        print("Дата введена не корректно")
#конец циклов проверки формата даты
print(username ,title, content, status,created_date, issue_date, sep='\n')

