import json
import os
import hashlib


BLOCK_CHAIN_DIRECTION = os.path.abspath(os.curdir) + r'\blockchain'


def get_hash(student_folder, filename):
    file = open(BLOCK_CHAIN_DIRECTION + r'\{}'.format(student_folder) + r'\{}'.format(filename), 'rb').read()

    return hashlib.sha256(file).hexdigest()


def get_files(student_folder):
    if os.path.exists(BLOCK_CHAIN_DIRECTION + r'\{}'.format(student_folder)):
        files = os.listdir(BLOCK_CHAIN_DIRECTION + r'\{}'.format(student_folder))
    else:
        os.mkdir(BLOCK_CHAIN_DIRECTION + r'\{}'.format(student_folder))
        files = os.listdir(BLOCK_CHAIN_DIRECTION + r'\{}'.format(student_folder))
    return files


def sort_files(student_folder):
    files = get_files(student_folder)
    number_of_file = []
    for i in files:
        i = int(i)
        number_of_file.append(i)
    number_of_file.sort()

    if len(number_of_file) != 0:
        last_file = number_of_file[-1]
        filename = str(last_file + 1)

        return last_file, filename


def block_check(student_folder):
    files = get_files(student_folder)
    number_of_file = []
    for i in files:
        i = int(i)
        number_of_file.append(i)
    number_of_file.sort()

    result = []

    for elem in number_of_file[1:]:
        hsh = json.load(open(BLOCK_CHAIN_DIRECTION + r'\{}'.format(student_folder) + r'\{}'.format(elem)))['Хэш']

        last_file = str(elem - 1)
        actual_hash = get_hash(student_folder, last_file)

        if actual_hash == hsh:
            res = 'Всё в порядке'
        else:
            res = 'Изменен'

        result.append({'Блок': last_file, 'Результат': res})

    return result


def write_block(f_and_s_name, lesson, mark, date, prev_hash=''):

    f_and_s_name = f_and_s_name.upper()
    files = get_files(student_folder=f_and_s_name)

    if len(files) == 0:

        data = {
            'Фамилия, имя': f_and_s_name,
            'Урок': lesson,
            'Оценка': mark,
            'Дата': date,
            'Хэш': prev_hash
        }

        with open(BLOCK_CHAIN_DIRECTION + r'\{}'.format(f_and_s_name) + r'\1', 'w', encoding='cp1251') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    else:

        last_file, filename = sort_files(student_folder=f_and_s_name)

        prev_hash = get_hash(f_and_s_name, last_file)

        data = {
            'Фамилия, имя': f_and_s_name,
            'Урок': lesson,
            'Оценка': mark,
            'Дата': date,
            'Хэш': prev_hash
        }

        with open(BLOCK_CHAIN_DIRECTION + r'\{}'.format(f_and_s_name) + r'\{}'.format(filename), 'w', encoding='cp1251') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    write_block('ExaPLe1', 'Example', 'Example', 'Example')
    print(block_check(student_folder='ExaPLe1'))


if __name__ == '__main__':
    main()