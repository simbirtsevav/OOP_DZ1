student_list = []
lecturer_list = []
class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = ''
        student_list.append(self)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                (course in self.courses_in_progress or course in self.finished_courses) and (0 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return  print('Ошибка')

    def _average_score(self):
        score_list = []
        for grade in self.grades.values():
            for score in grade:
                score_list.append(score)
        num = 0
        for grade in score_list:
            num += grade
        return num / len(score_list)

    def __str__(self):
        self.average_grades = self._average_score()
        change_print = f'Имя: {self.name} \n'
        change_print1 = f'Фамилия: {self.surname} \n'
        change_print2 = f' средняя оценка за домашние задания: {self.average_grades} \n'
        change_print3 = f' курсы в процессе обучения: {",".join(self.courses_in_progress)} \n'
        change_print4 = f' завершенные курсы: {",".join(self.finished_courses)}'
        return change_print + change_print1  + change_print2 + change_print3 + change_print4

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f' {other} not a Student')
            return
        return float(self.average_grades) < float(other.average_grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = ''
        lecturer_list.append(self)

    def _average_score(self):
        score_list = []
        for grade in self.grades.values():
            for score in grade:
                score_list.append(score)
        num = 0
        for grade in score_list:
            num += grade
        return num / len(score_list)

    def __str__(self):
        self.average_grades = self._average_score()
        change_print = f'Имя: {self.name} \n'
        change_print1 = f'Фамилия: {self.surname} \n'
        change_print2 = f'Средняя оценка за лекции: {str(self.average_grades)}'
        return change_print + change_print1 + change_print2

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f' {other} not a Lecturer')
            return
        return float(self.average_grades) < float(other.average_grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        change_print = f'Имя: {self.name} \n'
        change_print1 = f'Фамилия: {self.surname}'
        return change_print + change_print1


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['git']
best_student.finished_courses += ['basic']
student2 = Student('second', 'student', 'male')
student2.courses_in_progress += ['git']
cool_reviewer = Reviewer('First', 'Reviewer')
reviewer2 = Reviewer('Second', 'Reviewer')
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['git']
lecturer2 = Lecturer('another', 'one')
lecturer2.courses_attached += ['git']
best_student.rate_hw(lecturer2, 'git', 5)
best_student.rate_hw(lecturer2, 'git', 8)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'git', 10)
best_student.rate_hw(cool_lecturer, 'git', 10)
best_student.rate_hw(cool_lecturer, 'git', 10)
student2.rate_hw(cool_lecturer, 'git', 5)
student2.rate_hw(cool_lecturer, 'git', 8)
cool_reviewer.rate_hw(best_student, 'Python', 3)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'git', 10)
cool_reviewer.rate_hw(student2, 'git', 2)
cool_reviewer.rate_hw(student2, 'git', 9)

def student_course_grade(students, course):
    course_grade = []
    for i in students:
         for grade in i.grades:
            if grade == course:
                course_grade.extend(i.grades[course])
    return print(f'средний бал по курсу {course}  у всех студентов: {sum(course_grade)/len(course_grade)}')

def lecturer_course_grade(lecturer, course):
    course_grade = []
    for i in lecturer:
         for grade in i.grades:
            if grade == course:
                course_grade.extend(i.grades[course])
    return print(f'средний бал по курсу {course}  у всех Лекторов: {sum(course_grade)/len(course_grade)}')

print(cool_lecturer.grades)
print(lecturer2.grades)
print(best_student.grades)
print(best_student.courses_in_progress)
print(cool_reviewer)
print(cool_lecturer)
print(lecturer2)
print(best_student)
print(student2)
print(lecturer2)
print(cool_lecturer < lecturer2)
print(best_student < student2)
student_course_grade(student_list, 'Python')
lecturer_course_grade(lecturer_list, 'git')

