import json
import os
import hashlib


BLOCK_CHAIN_DIRECTION = os.path.abspath(os.curdir) + r'\blockchain'


def get_hash(filename):
    file = open(BLOCK_CHAIN_DIRECTION + r'\{}'.format(filename), 'rb').read()

    return hashlib.md5(file).hexdigest()


def get_files():
    files = os.listdir(BLOCK_CHAIN_DIRECTION)
    return files


def sort_files():
    files = get_files()
    files = [int(i) for i in files]

    last_file = files[-1]
    filename = str(last_file + 1)

    return last_file, filename


def block_check():
    files = get_files()
    files = [int(i) for i in files]

    result = []

    for elem in files[1:]:
        hsh = json.load(open(BLOCK_CHAIN_DIRECTION + r'\{}'.format(elem)))['hash']  # n-го файла (без учета 1)

        last_file = str(elem - 1)
        actual_hash = get_hash(last_file)  # Хэш файла n - 1

        if actual_hash == hsh:
            res = 'Всё в порядке'
        else:
            res = 'Изменен'

        result.append({'Блок': last_file, 'Результат': res})

    return result


def write_block(name, lesson, mark, date, prev_hash=''):  # Тип даты дд.мм.гг

    files = sort_files()

    if len(files) == 0:
        data = {
            'name': name,
            'lesson': lesson,
            'mark': mark,
            'date': date,
            'hash': prev_hash
        }

        with open(BLOCK_CHAIN_DIRECTION + r'\1', 'w', encoding='cp1251') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    else:

        last_file, filename = sort_files()

        prev_hash = get_hash(str(last_file))
        data = {
            'name': name,
            'lesson': lesson,
            'mark': mark,
            'date': date,
            'hash': prev_hash
        }

        with open(BLOCK_CHAIN_DIRECTION + r'\{}'.format(filename), 'w', encoding='cp1251') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    print(block_check())
    write_block('Example', 'Example', 'Example', 'Example')


if __name__ == '__main__':
    main()