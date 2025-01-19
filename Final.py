note = {}
username = input('Введите имя: ')
content = input('Описание заметки: ')
status = input('Статус заметки: ')
import datetime
while True:
    created_date = input('Дата заметки в формате (день.месяц.год),например 10.11.2024: ')
    try:
        datetime.datetime.strptime(created_date,'%d.%m.%Y')
        print('Введена корректная дата')
        break
    except ValueError:
        print("Дата введена не корректно")
while True:
    issue_date = input('Дедлайн в формате (день.месяц.год),например 18.01.2025: ')
    try:
        datetime.datetime.strptime(issue_date, '%d.%m.%Y')
        print('Введена корректная дата')
        break
    except ValueError:
        print("Дата введена не корректно")
titles = []
titles.append(input('Заголовок заметки 1: '))
titles.append(input('Заголовок заметки 2: '))
titles.append(input('Заголовок заметки 3: '))
note['username'] = username
note['content'] = content
note['status'] = status
note['created_date'] = created_date
note['issue_date'] = issue_date
note['titles'] = titles
print('Имя:', note['username'],end='\n')
print('Заголовки заметок:', note['titles'],end='\n')
print('Содержание заметки:', note['content'],end='\n')
print('Статус заметки:', note['status'],end='\n')
print('Дата заметки:', note['created_date'][:5], end='\n')
print('Дата дедлайна:', note['issue_date'][:5], end='\n')