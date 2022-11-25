class Student:
    student_list=[]
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)


    def rate_lec(self, teacher, course, grade):
        if isinstance(teacher, Lecturer) and course in self.courses_in_progress and course in teacher.courses_attached:
            if course in teacher.grades:
                teacher.grades[course] += [grade]
            else:
                teacher.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self, grades):
        a = 0
        b = 0
        for key in grades:
            a += (len(grades[key]))
            b += (sum(grades[key]))
        return round(b / a, 1)

    def __str__(self):
        fc = ', '.join(self.finished_courses)
        cp = ', '.join(self.courses_in_progress)
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.average_rate(self.grades)}\n'
               f'Курсы в процессе изучения: {cp}\n'
               f'Завершенные курсы: {fc}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.average_rate(self.grades) < other.average_rate(other.grades)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def aagrade(self, grades):
        a=0
        b=0
        for key in grades:
            a += (len(grades[key]))
            b += (sum(grades[key]))
        return round(b / a, 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.aagrade(self.grades) < other.aagrade(other.grades)


    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.aagrade(self.grades)}')
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res


anton_astakhov = Student('Антон', 'Астахов', 'male')
anton_astakhov.courses_in_progress += ['Welcome Python', 'Python OOP']
anton_astakhov.courses_in_progress += ['GIT']
anton_astakhov.finished_courses += ['Python Beginner']

vladimir_konkov = Student('Владимир','Коньков','male')
vladimir_konkov.courses_in_progress += ['Python OOP', 'GIT', 'Python Beginner']
vladimir_konkov.finished_courses += ['Welcome Python']

oleg_bulygin = Lecturer('Олег','Булыгин')
oleg_bulygin.courses_attached += ['Python OOP', 'GIT']

alex_bardin = Lecturer('Александр','Бардин')
alex_bardin.courses_attached += ['Python Beginner', 'Welcome Python']

alena_batitskaya = Reviewer('Алена','Батитская')
alena_batitskaya.courses_attached += ['GIT']

evgeniy_shmargunov = Reviewer('Евгений','Шмаргунов')
evgeniy_shmargunov.courses_attached += ['Welcome Python', 'Python OOP']

alena_batitskaya.rate_hw(anton_astakhov, 'GIT', 9)
alena_batitskaya.rate_hw(vladimir_konkov, 'GIT', 8)
evgeniy_shmargunov.rate_hw(anton_astakhov, 'Welcome Python', 8)
evgeniy_shmargunov.rate_hw(vladimir_konkov, 'Python OOP', 8)

anton_astakhov.rate_lec(oleg_bulygin, 'Python OOP', 10)
anton_astakhov.rate_lec(alex_bardin, 'Welcome Python', 9)
vladimir_konkov.rate_lec(alex_bardin, 'Python Beginner', 9)
vladimir_konkov.rate_lec(oleg_bulygin, 'GIT', 9)


print(anton_astakhov)
print()
print(vladimir_konkov)
print()
print(oleg_bulygin)
print()
print(alex_bardin)
print()
print(alena_batitskaya)
print()
print(evgeniy_shmargunov)
print()
print(anton_astakhov < vladimir_konkov)
print()
print(oleg_bulygin > alex_bardin)



def average_rate(students):
    sum_of_all_sudents_rates = 0
    average_rate = 0
    for student in students:
        sum_of_all_sudents_rates+= student.average_rate(student.grades)
    return round(sum_of_all_sudents_rates / len(students), 1)



students=[anton_astakhov,vladimir_konkov]

averageStudentsRate=average_rate(students)
print(averageStudentsRate)
