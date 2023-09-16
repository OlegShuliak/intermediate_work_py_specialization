from file_worker import add_to_file, read_file
import datetime
import random
import os


def add_note():
    name = input('Введите заголовок заметки: ')
    msg = input('Оcтавте заметку: ')
    date = f'{datetime.datetime.now()}'
    id = random.randint(1000, 10000)
    return dict(id=id, name=name, body=msg, date=date)


def save_note(file_name, note):
    if os.path.exists(file_name):
        note_list = read_file(file_name)
        note_list.append(note)
        add_to_file(file_name, note_list)
    else:
        note_list = [note]
        add_to_file(file_name, note_list)
    print(f'Заметка успешно сохранена в файл {file_name}.')


def del_note(file_name, note_id):
    if os.path.exists(file_name):
        note_list = read_file(file_name)
        check_len = len(note_list)
        for dictionary in note_list:
            if note_id == dictionary.get('id'):
                note_list.remove(dictionary)
                print(f'Заметка с id={note_id} удалена.')
        if check_len == len(note_list):
            print(f'Заметка с id={note_id} в файле {file_name} не существует.')
        else:
            add_to_file(file_name, note_list)
    else:
        print(f'Файла {file_name} не существует.')


def read_all_notes(file_name):
    if os.path.exists(file_name):
        note_list = read_file(file_name)
        for dictionary in note_list:
            print(f'{dictionary};')
    else:
        print(f'Файла {file_name} с заметками не существует.')


def mod_note_id(file_name, note_id):
    if os.path.exists(file_name):
        note_list = read_file(file_name)
        for dictionary in note_list:
            if note_id == dictionary.get('id'):
                dictionary['body'] = input('Измените запись в заметке: ')
                dictionary['date'] = f'{datetime.datetime.now()}'
                print(f'Заметка с id={note_id} изменена.')
        add_to_file(file_name, note_list)


if __name__ == '__main__':
    note = add_note()
    print(note)
    save_note('new_note.json', note)
    del_note('new_note.json', 9284)
    read_all_notes('new_note.json')
    mod_note_id('new_note.json', 8715)
