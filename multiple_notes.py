notes = []
# импорт библиотеки datetime
import datetime


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


# добавляем цикл для создания и удаления заметок
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
