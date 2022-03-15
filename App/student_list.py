students_file = 'student_name.txt'
student_list = []


def add_student(student_inf):
    with open(students_file, 'w', encoding='cp1251') as write_file:
        write_file.write(student_inf)


def get_info():
    with open(students_file, 'r', encoding='cp1251') as read_file:
        for line in read_file:
            if len(line) != '':
                student_list.append(line)
    return student_list[-1]