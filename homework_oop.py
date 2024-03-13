# Класс студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Функция выставления оценок лекторам
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 0 < grade < 11:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Функция вывода информации о студенте
    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за задания: {average_grade(self.grades)}'
                  f'\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}'
                  f'\nЗавершенные курсы: {', '.join(self.finished_courses)}')
        return result

    # Функция сравнения средних оценок студентов
    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return average_grade(self.grades) < average_grade(other_student.grades)


# Родительский класс преподавателей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Класс ревьюеров
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Функция выставления оценок студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Функция вывода информации о ревьюерах
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


# Класс лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Функция вывода информации о лекторах
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades)}'
        return result

    # Функция сравнения средней оценки лекторов
    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return average_grade(self.grades) > average_grade(other_lecturer.grades)


# Функция вычисления средней оценки (общая)
def average_grade(grades):
    if type(grades) is dict:
        grades_list = []
        for key, value in grades.items():
            grades_list.extend(value)
        result = round(sum(grades_list) / len(grades_list), 1)
        return result
    elif type(grades) is list:
        result = round(sum(grades) / len(grades), 1)
        return result


# Создание экземпляров класса Student
some_student = Student('Ruoy', 'Eman', 'Male')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
some_student1 = Student('Ken', 'Block', 'Male')
some_student1.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['API']
some_student1.finished_courses += ['Введение в программирование']
some_student1.finished_courses += ['Git']
some_students_list = [some_student, some_student1]

# Создание экземпляров класса Reviewer
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer.courses_attached += ['Введение в программирование']

# Создание экземпляров класса Lecturer
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
some_lecturer.courses_attached += ['Введение в программирование']
some_lecturer1 = Lecturer('Brat', 'Hart')
some_lecturer1.courses_attached += ['Python']
some_lecturer1.courses_attached += ['Git']
some_lecturer1.courses_attached += ['Введение в программирование']
some_lecturers_list = [some_lecturer, some_lecturer1]

# Выставление оценок лекторам
some_student.rate_lec(some_lecturer, 'Python', 7)
some_student.rate_lec(some_lecturer, 'Git', 8)
some_student1.rate_lec(some_lecturer1, 'Python', 10)
some_student1.rate_lec(some_lecturer1, 'Git', 9)

# Выставление оценок студентам
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer.rate_hw(some_student1, 'Python', 10)
some_reviewer.rate_hw(some_student1, 'Git', 9)


# Функция вычисления средней оценки (по курсам)
def average_course_grade(all_students, current_course):
    all_course_grades = []
    for current_student in all_students:
        if current_course in current_student.grades.keys():
            for every_grade in current_student.grades.get(current_course):
                all_course_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у студента {current_student.name} {current_student.surname}')
    return average_grade(all_course_grades)


# Функция вычисления средней оценки (по лекторам)
def average_lecturer_grades(all_lecturers, current_course):
    all_course_grades = []
    for current_lecturer in all_lecturers:
        if current_course in current_lecturer.grades.keys():
            for every_grade in current_lecturer.grades.get(current_course):
                all_course_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у лектора {current_lecturer.name} {current_lecturer.surname}')
    return average_grade(all_course_grades)


print(some_reviewer)
print('-----------------')
print(some_lecturer)
print('-----------------')
print(some_student)
print('-----------------')
print(some_student1 > some_student)
print(some_lecturer < some_lecturer1)
print('-----------------')
print(f'Средняя оценка за домашние задания по курсу Python: {average_course_grade(some_students_list, 'Python')}')
print(
    f'Средняя оценка за лекции всех лекторов по курсу Python: {average_lecturer_grades(some_lecturers_list, 'Python')}')
