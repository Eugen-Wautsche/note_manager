notes = {}
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
            #Добавляем второй цикл для ответа на ввод ДА\НЕТ, иначе перебросит на ввод заголовка,(так не пойдёт)
            # если неправильно введём ДА\НЕТ
            while True:
                change_status = input("Хотите изменить статус заметки? (да/нет): ")
                if change_status.lower() == 'да':
                    status = input("Введите новый статус заметки: ")
                    notes[title] = status
                #используем для выхода из цикла ДА
                    break
                # else if как условный оператор цикла для ответа (нет)
                elif change_status.lower() == 'нет':
                    print("Статус заметки не изменён.")
                #используем для выхода из цикла НЕТ
                    break
                else:
                    print("Пожалуйста, введите (да/нет)")
                #НЕ используем break для выхода из цикла чтобы зациклить ДА\НЕТ
print("Список заметок и их статус:")
for title, status in notes.items():
    print(f"(заметка) {title} -> (статус) {status}")