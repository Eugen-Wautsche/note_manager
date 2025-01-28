# импорт библиотеки datetime
import datetime

# добавляем список notes
notes = []


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
        # убираем ручной ввод даты (дата создания заметки = текущая дата)
        while True:
            deadline = input('Дедлайн в формате (день.месяц.год),например 18.01.2025: ')
            try:
                deadline = datetime.datetime.strptime(deadline, '%d.%m.%Y')
                # Думал добавить сравнение текущей даты и дедлайна, чтобы дедлайн не был раньше текущей даты,
                # но есть статус 'выполнено'
                # if deadline < datetime.datetime.now():
                # print("Дата дедлайна не может быть раньше текущей даты. Пожалуйста, введите дату заново.")
                # continue
                print('Введена корректная дата')
                break
            except ValueError:
                print("Дата введена не корректно")
        note = {
            "name": name,
            "title": title,
            "description": description,
            "status": status,
            # меняем в словаре
            # дата создания заметки = текущая дата в том же формате, без времени
            "created_date": datetime.datetime.now().strftime('%d.%m.%Y'),
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
    # выводим дату создания заметки
    print(f"Дата создания заметки: {note['created_date']}")
    print(f"Дедлайн: {note['deadline']}")
    print()
