from notes_worker import add_note, save_note, del_note, read_all_notes, mod_note_id, show_notes_date, show_note_id

file_name = 'my_notes.json'
command = True

while command:
    print('Выберите команду для работы с заметками:')
    print('1 - Добавить новую заметку;')
    print('2 - Изменить существующую заметку по id;')
    print('3 - Удалить заметку по id;')
    print('4 - Показать заметку по id;')
    print('5 - Показать все заметки;')
    print('6 - Сделать выборку заметок по дате;')
    print('0 - завершить работу программы.')

    try:
        command = int(input('Введите номер команды: '))

        if command == 1:
            new_note = add_note()
            save_note(file_name, new_note)
        elif command == 2:
            note_id = int(input('Введите id заметки: '))
            mod_note_id(file_name, note_id)
        elif command == 3:
            note_id = int(input('Введите id заметки: '))
            del_note(file_name, note_id)
        elif command == 4:
            note_id = int(input('Введите id заметки: '))
            show_note_id(file_name, note_id)
        elif command == 5:
            read_all_notes(file_name)
        elif command == 6:
            date = input('Введите дату для поиска заметок в формате yyyy-mm-dd: ')
            if len(date) == 10:
                show_notes_date(file_name, date)
            else:
                print('Неверно введена дата.')
        elif command < 0 or 6 < command:
            print('Некорректный ввод команды, повторите попытку ввода.')

    except ValueError:
        print('Некорректный ввод команды, повторите попытку ввода.')
