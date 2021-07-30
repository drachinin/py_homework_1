def average_grade(person):
    sum_grades = 0
    len_values = 0
    for value in person.grades.values():
        len_values += len(value)
        for i in value:
            sum_grades += i
    return round((sum_grades / len_values), 1)

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

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('John', 'Cena')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lc(cool_lecturer, 'Python', 10)
best_student.rate_lc(cool_lecturer, 'Python', 5)
best_student.rate_lc(cool_lecturer, 'Python', 1)
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 6)
 
print(best_student)

print(cool_reviewer)

print(cool_lecturer)

