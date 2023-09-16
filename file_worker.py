import json


def add_to_file(file_name, note):
    with open(file_name, 'w') as f:
        json.dump(note, f)



def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            notes = json.load(f)
            return notes
    except FileNotFoundError:
        print('Данного файла с заметками не существует, выберите другой файл либо создайте новый')
        pass


if __name__ == '__main__':
    add_to_file('notes.json', {'name': 'leo'})
    notes1 = read_file('notes.json')
    print(notes1)
