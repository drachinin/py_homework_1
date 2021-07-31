def average_grade(person):
    sum_grades = 0
    len_values = 0
    for value in person.grades.values():
        len_values += len(value)
        for i in value:
            sum_grades += i
    return round((sum_grades / len_values), 1)

def average_grade_students(students, course):
    average_grades = 0
    student_id = 0
    for student in students:
        if not isinstance(student, Student) and course in student.courses_in_progress and course in student.finished_courses:
            print('Не студенты')
            return
        student_id += 1
        average_grades += average_grade(student)
        return round(average_grades / student_id, 1)

def average_grade_lecturers(lecturers, course) :
    average_grades = 0
    lecturer_id = 0
    for lecturer in lecturers:
        if not isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            print('Не студенты')
            return
        lecturer_id += 1
        average_grades += average_grade(lecturer)
        return round(average_grades / lecturer_id, 1)


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 0 < grade < 11:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {average_grade(self)}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        if average_grade(self) > average_grade(other):
            print(f'У студента {self.name} средняя оценка выше')
            return
        else:
            print(f'У студента {other.name} средняя оценка выше')

        
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {average_grade(self)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        if average_grade(self) > average_grade(other):
            print(f'У лектора {self.name} средняя оценка выше')
            return
        else:
            print(f'У лектора {other.name} средняя оценка выше')

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

bad_student = Student('Name', 'Surname', 'Gender')
bad_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('John', 'Cena')
cool_lecturer.courses_attached += ['Python']

bad_lecturer = Lecturer('Michael', 'Jackson')
bad_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

bad_reviewer = Reviewer('Bad', 'Reviewer')
bad_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(bad_student, 'Python', 3)
cool_reviewer.rate_hw(bad_student, 'Python', 1)
cool_reviewer.rate_hw(bad_student, 'Python', 2)

best_student.rate_lc(bad_lecturer, 'Python', 1)
best_student.rate_lc(bad_lecturer, 'Python', 2)
best_student.rate_lc(bad_lecturer, 'Python', 1)

best_student.rate_lc(cool_lecturer, 'Python', 10)
best_student.rate_lc(cool_lecturer, 'Python', 5)
best_student.rate_lc(cool_lecturer, 'Python', 1)
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 6)
 
print(best_student)

print(cool_reviewer)

print(cool_lecturer)

bad_lecturer > cool_lecturer

bad_student > best_student

