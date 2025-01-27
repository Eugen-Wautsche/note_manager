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
