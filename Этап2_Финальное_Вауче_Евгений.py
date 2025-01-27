# 1. add_titles_loop.py: Цикл для добавления заголовков
# код запрашивает у пользователя заголовки и добавляет их в список titles
titles = []
# создаём множество уникальных заголовков
unique_titles = set()
while True:
    title = input("Введите заголовок. Команда 'стоп' или пустой ввод используется для завершения: ")
    if title.lower() == 'стоп' or title == '':
        break
        # обрабатывает ввод пользователя и не добавляет лишние пустые значения в список
    if title.strip() != '':
        # проверка на уникальность заголовка
        if title not in unique_titles:
            titles.append(title)
            unique_titles.add(title)
        else:
            print("Этот заголовок уже существует.")
# использую метод join(), чтобы вывести заголовки без квадратных скобок
print("Список заголовков:", ", ".join(titles))

# 2.update_status.py: Проверка и обновление статуса заметки
# код запрашивает у пользователя заголовки и добавляет их в словарь notes
notes = {}
# первый цикл ввода данных
while True:
    title = input("Введите заголовок заметки. Команда 'стоп' или пустой ввод используется для завершения: ")
    if title.lower() == 'стоп' or title == '':
        break
    if title.strip() != '':
        if title not in notes:
            status = input("Введите статус заметки: ")
            notes[title] = status
        else:
            print("Этот заголовок уже существует.")
# второй цикл для изменения статуса заметки
while True:
    change_status = input("Хотите изменить статус заметки? (да/нет): ")
    if change_status.lower() == 'да':
        title = input("Введите заголовок заметки, которую хотите изменить: ")
        # обращаемся за заголовками в словарь
        if title in notes:
            print("Выберите новый статус заметки:\n1. выполнено\n2. в процессе\n3. отложено")
            new_status = input("Ваш выбор: ")
            if new_status == '1':
                notes[title] = 'выполнено'
            elif new_status == '2':
                notes[title] = 'в процессе'
            elif new_status == '3':
                notes[title] = 'отложено'
            elif new_status.lower() == 'выполнено':
                notes[title] = 'выполнено'
            elif new_status.lower() == 'в процессе':
                notes[title] = 'в процессе'
            elif new_status.lower() == 'отложено':
                notes[title] = 'отложено'
            else:
                print("Некорректный выбор. Статус заметки не изменён.")
                continue  # добавлено для продолжения цикла при некорректном выборе
            break  # добавлено для выхода из цикла после успешного изменения статуса
        else:
            print("Заметка с таким заголовком не найдена.")
    elif change_status.lower() == 'нет':
        print("Статус заметки не изменён.")
        break
    else:
        print("Пожалуйста, введите (да/нет)")
print("Список заметок и их статус:")
for title, status in notes.items():
    print(f"(заметка) {title} -> (статус) {status}")

# 3.check_deadline.py: Обработка дедлайнов
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
            # обрабатываем исключение (конструкция кода из предыдущих заданий)
        except ValueError:
            print("Пожалуйста, введите дату в формате день.месяц.год, например: 10.12.2024.")


# проверка истечения дедлайна
def check_deadline(issue_date):
    current_date = get_current_date()
    # вычисляем разницу между двумя датами
    date_difference = calculate_date_difference(current_date, issue_date)
    if date_difference < 0:
        print("Внимание! Дедлайн истёк", abs(date_difference), "дней назад.")
    elif date_difference == 0:
        print("Дедлайн сегодня!")
    else:
        print("До дедлайна осталось", date_difference, "дней.")


# функция запуска программы
def run_program():
    print("Добро пожаловать в программу проверки дедлайна!")
    # выводим текущую дату
    print("Текущая дата:", get_current_date().strftime("%d.%m.%Y"))
    issue_date = get_user_input()
    check_deadline(issue_date)


run_program()
# конец задания check_deadline

# 4. multiple_notes.py: Работа с несколькими заметками
# добавляем список notes
notes = []
# импорт библиотеки datetime выполнен ранее
# функция создания заметки + проверка формата даты из final
# так же используем конструкцию кода из предыдущих заданий в последующих функциях
# проверяем операторы цикла в случае багов добавляем/меняем/удаляем
def create_note():
    while True:
        # в случае если перед полем ввода строка слишком длинная,
        # учту в следующих заданиях(оставьте, пожалуйста, комментарий)
        name = input("Введите имя пользователя (в случае пустого ввода, запросим информацию заново): ")
        if name == "":
            continue
        title = input("Введите заголовок заметки (в случае пустого ввода, запросим информацию заново): ")
        if title == "":
            continue
        if any(note['title'] == title for note in notes):
            print("Заголовок уже существует. Пожалуйста, введите другой заголовок.")
            continue
        description = input("Введите описание заметки: ")
        if description == "":
            print("Пожалуйста, введите описание заметки.")
            continue
        while True:
            status = input("Введите статус заметки (новая, в процессе, выполнено): ")
            if status.lower() in ['новая', 'в процессе', 'выполнено']:
                break
            else:
                print("Статус введен некорректно. Пожалуйста, введите 'новая', 'в процессе' или 'выполнено'.")
        while True:
            created_date = input('Дата заметки в формате (день.месяц.год),например 10.11.2024: ')
            try:
                created_date = datetime.datetime.strptime(created_date, '%d.%m.%Y')
                print('Введена корректная дата')
                break
            except ValueError:
                print("Дата введена не корректно")
        while True:
            deadline = input('Дедлайн в формате (день.месяц.год),например 18.01.2025: ')
            try:
                deadline = datetime.datetime.strptime(deadline, '%d.%m.%Y')
                print('Введена корректная дата')
                break
            except ValueError:
                print("Дата введена не корректно")
        note = {
            "id": len(notes) + 1,
            "name": name,
            "title": title,
            "description": description,
            "status": status,
            "creation_date": created_date.strftime('%d.%m.%Y'),
            "deadline": deadline.strftime('%d.%m.%Y')
        }
        return note


# функция удаления заметки по ID
def delete_note(note_id):
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            print(f"Заметка с ID {note_id} удалена.")
            return
    print("Заметка с таким ID не найдена.")


# цикл для создания заметок
while True:
    print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")
    add_note = input("Хотите добавить заметку? (да/нет): ")
    if add_note.lower() == "да":
        note = create_note()
        notes.append(note)
    elif add_note.lower() == "нет":
        print("Заметка не добавлена.")
        break
    elif add_note == "":
        continue
    else:
        print("Пожалуйста, введите 'да' или 'нет'.")
print("Список заметок:")
for note in notes:
    print(f"ID заметки: {note['id']}")
    print(f"Имя пользователя: {note['name']}")
    print(f"Заголовок заметки: {note['title']}")
    print(f"Описание заметки: {note['description']}")
    print(f"Статус заметки: {note['status']}")
    print(f"Дата создания: {note['creation_date']}")
    print(f"Дедлайн: {note['deadline']}")
    print()
# цикл удаления заметок
while True:
    delete_note = input("Хотите удалить заметку? (да/нет): ")
    if delete_note.lower() == "да":
        note_id = int(input("Введите ID заметки, которую хотите удалить: "))
        for note in notes:
            if note['id'] == note_id:
                notes.remove(note)
                print(f"Заметка с ID {note_id} удалена.")
        print("Заметка с таким ID не найдена.")
    elif delete_note.lower() == "нет":
        print("Заметка не удалена.")
        break
    elif delete_note == "":
        continue
    else:
        print("Пожалуйста, введите 'да' или 'нет'.")
print("Список заметок после удаления:")
for note in notes:
    print(f"ID заметки: {note['id']}")
    print(f"Имя пользователя: {note['name']}")
    print(f"Заголовок заметки: {note['title']}")
    print(f"Описание заметки: {note['description']}")
    print(f"Статус заметки: {note['status']}")
    print(f"Дата создания: {note['creation_date']}")
    print(f"Дедлайн: {note['deadline']}")
    print()

#5. delete_note.py: Удаление заметок
# добавляем список notes
notes = []
# импорт библиотеки datetime выполнен ранее


# функция удаления заметки по имени пользователя или заголовку без учёта регистра
def delete_note():
    while True:
        name = input("Введите имя пользователя или заголовок заметки для удаления: ")
        if name == "":
            continue
        for note in notes:
            if note['name'].lower() == name.lower() or note['title'].lower() == name.lower():
                notes.remove(note)
                print("Заметка успешно удалена.")
                return
        print("Заметка не найдена. Пожалуйста, введите имя пользователя или заголовок заметки.")


# функция создания заметки + проверка формата даты из final
def create_note():
    while True:
        name = input("Введите имя пользователя (в случае пустого ввода, запросим информацию заново): ")
        if name == "":
            continue
        title = input("Введите заголовок заметки (в случае пустого ввода, запросим информацию заново): ")
        if title == "":
            continue
        if any(note['title'] == title for note in notes):
            print("Заголовок уже существует. Пожалуйста, введите другой заголовок.")
            continue
        description = input("Введите описание заметки: ")
        if description == "":
            print("Пожалуйста, введите описание заметки.")
            continue
        while True:
            status = input("Введите статус заметки (новая, в процессе, выполнено): ")
            if status.lower() in ['новая', 'в процессе', 'выполнено']:
                break
            else:
                print("Статус введен некорректно. Пожалуйста, введите 'новая', 'в процессе' или 'выполнено'.")
        while True:
            created_date = input('Дата заметки в формате (день.месяц.год),например 10.11.2024: ')
            try:
                created_date = datetime.datetime.strptime(created_date, '%d.%m.%Y')
                print('Введена корректная дата')
                break
            except ValueError:
                print("Дата введена не корректно")
        while True:
            deadline = input('Дедлайн в формате (день.месяц.год),например 18.01.2025: ')
            try:
                deadline = datetime.datetime.strptime(deadline, '%d.%m.%Y')
                print('Введена корректная дата')
                break
            except ValueError:
                print("Дата введена не корректно")
        note = {

            "name": name,
            "title": title,
            "description": description,
            "status": status,
            "creation_date": created_date.strftime('%d.%m.%Y'),
            "deadline": deadline.strftime('%d.%m.%Y')
        }
        return note


# цикл для создания заметок
while True:
    print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")
    add_note = input("Хотите добавить заметку? (да/нет): ")
    if add_note.lower() == "да":
        note = create_note()
        notes.append(note)
    elif add_note.lower() == "нет":
        print("Заметка не добавлена.")
        break
    elif add_note == "":
        continue
    else:
        print("Пожалуйста, введите 'да' или 'нет'.")
print("Список заметок:")
for note in notes:
    print(f"Имя пользователя: {note['name']}")
    print(f"Заголовок заметки: {note['title']}")
    print(f"Описание заметки: {note['description']}")
    print(f"Статус заметки: {note['status']}")
    print(f"Дата создания: {note['creation_date']}")
    print(f"Дедлайн: {note['deadline']}")
    print()

# цикл для удаления заметок
while True:
    print("Вы можете удалить заметку.")
    delete_note_option = input("Хотите удалить заметку? (да/нет): ")
    if delete_note_option.lower() == "да":
        delete_note()
    elif delete_note_option.lower() == "нет":
        print("Заметка не удалена.")
        break
    elif delete_note_option == "":
        continue
    else:
        print("Пожалуйста, введите 'да' или 'нет'.")
print("Список заметок после удаления:")
for note in notes:
    print(f"Имя пользователя: {note['name']}")
    print(f"Заголовок заметки: {note['title']}")
    print(f"Описание заметки: {note['description']}")
    print(f"Статус заметки: {note['status']}")
    print(f"Дата создания: {note['creation_date']}")
    print(f"Дедлайн: {note['deadline']}")
    print()
#Этап1_Финальное_Вауче_Евгений.py <- FINAL